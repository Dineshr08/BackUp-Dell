import {users} from './constants.mjs';

export const getIndexByID = (req, res, next) => {

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

  req.userIndex = userIndex; //- Appended back to req
  next();

}