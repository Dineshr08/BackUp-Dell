import { Router } from "express";
import { users } from "../utils/constants.mjs";
import { createUserValidation } from "../utils/validationSchemas.mjs";
import { checkSchema, validationResult, matchedData } from "express-validator";
import { getIndexByID } from "../utils/middleware.mjs";
const router = Router();

router.get("/api/users", (req, res) => {
  req.sessionStore.get(req.session.id, (err, sessionData)=>{
    if(err) {
      console.log('msg:', err)
    } else {
      console.log(sessionData);
    }
  })
  console.log(req.query);
  console.log(req.cookies);

  if (req.signedCookies && req.signedCookies.user === "Admin1") {
    const { filter, value } = req.query;
    console.log(filter, value);
    let result = users;

    if (filter && value) {
      result = users.filter((user) => {
        return user[filter].toLowerCase().includes(value.toLocaleLowerCase());
      });
    }
    res.send(result);
  } else {
    res
      .status(404)
      .send({ msg: "You dont have permission to perform this operation" });
  }
});

router.get("/api/users/:id", (req, res) => {
  const userID = parseInt(req.params.id);

  if (isNaN(userID)) {
    return res
      .status(400)
      .send({ msg: "Bad Request, Please check the input user id" });
  }

  const user = users.find((user) => user.id === userID);
  if (user) {
    return res.send(user);
  }

  res.status(404).send({ msg: "User Not Found" });
});

router.post("/api/users", checkSchema(createUserValidation), (req, res) => {
  const result = validationResult(req);
  console.log(result);
  if (!result.isEmpty()) {
    return res.status(400).send({ error: result.array() });
  }
  console.log(req.body);

  const body = matchedData(req);
  const newUser = { id: users[users.length - 1].id + 1, ...body };
  console.log(newUser);
  users.push(newUser);
  console.log(users);
  res.status(201).send(users);
});

router.put("/api/users/:id", (req, res) => {
  const userID = parseInt(req.params.id);

  if (isNaN(userID)) {
    return res
      .status(400)
      .send({ msg: "Bad Request, Please check the input user id" });
  }

  const userIndex = users.findIndex((user) => user.id === userID);
  if (userIndex === -1) {
    res.status(404).send({ msg: "User Not Found" });
  }

  const { body } = req;
  users[userIndex] = { id: userID, ...body };
  return res.status(200).send(users);
});

router.patch("/api/users/:id", (req, res) => {
  const userID = parseInt(req.params.id);

  if (isNaN(userID)) {
    return res
      .status(400)
      .send({ msg: "Bad Request, Please check the input user id" });
  }

  const userIndex = users.findIndex((user) => user.id === userID);
  if (userIndex === -1) {
    res.status(404).send({ msg: "User Not Found" });
  }

  const { body } = req;
  users[userIndex] = { ...users[userIndex], ...body };
  return res.status(200).send(users);
});

router.patch("/api/users/:id", getIndexByID, (req, res) => {
  const userIndex = req.userIndex;

  const { body } = req;
  users.splice(userIndex, 1);
  return res.status(200).send(users);
});

export default router;
