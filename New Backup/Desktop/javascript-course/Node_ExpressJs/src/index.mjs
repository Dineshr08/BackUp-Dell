/*
//Route Parameter
import express from "express";

const app = express();

const PORT = 3000;

app.listen(PORT, () => {
  console.log(`Application is Running on ${PORT}`);
});

const users = [
  { id: 1, userName: "Dinesh" },
  { id: 2, userName: "Thilaga" },
  { id: 3, userName: "Diya" },
  { id: 4, userName: "Rajendran" },
  { id: 5, userName: "Kala" },
  { id: 6, userName: "Abinaya" },
  { id: 7, userName: "Tamil" },
];

app.get("/api/users", (req, res) => {
  res.send(users);
});
app.get("/api/users/:id", (req, res) => {
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
*/

//Query Parameter

//api/products?filter=productName&value=mo;
//api/users?filter=userName&value=di;

import express from "express";

// import {createUserValidation} from './utils/validationSchemas.mjs';
// import { checkSchema, validationResult, matchedData } from "express-validator";
import routers from "./routes/router.mjs";
import session from "express-session";
//Cookies:
import cookieParser from "cookie-parser";
const app = express();
app.use(express.json());
app.use(cookieParser('nodejs'))
app.use(session({
  secret: "hello secret",
  saveUninitialized: false,
  resave: false,
  cookie: {
    maxAge: 3600000
  }
}))
app.use(routers);

const PORT = 3000;

app.get("/", (req, res) => {
  res.cookie('user','Admin', {maxAge:3600000, signed:true});
  res.send({ msg: "Welocme Root" });
});
app.listen(PORT, () => {
  console.log(`Application is Running on ${PORT}`);
});

// //Route course comment start here
// const users = [
//   { id: 1, userName: "Dinesh" },
//   { id: 2, userName: "Thilaga" },
//   { id: 3, userName: "Diya" },
//   { id: 4, userName: "Rajendran" },
//   { id: 5, userName: "Kala" },
//   { id: 6, userName: "Abinaya" },
//   { id: 7, userName: "Tamil" },
// ];

// const products = [
//   { id: 1, productName: "Laptop" },
//   { id: 2, productName: "Mobile" },
//   { id: 3, productName: "Desktop" },
//   { id: 4, productName: "iPad" },
// ];

// ////Different way of handeling middleware Step2:
// const getIndexByID = (req, res, next) => {

//   const userID = parseInt(req.params.id);

//   if (isNaN(userID)) {
//     return res
//       .status(400)
//       .send({ msg: "Bad Request, Please check the input user id" });
//   }

//   const userIndex = users.findIndex((user) => user.id === userID);
//   if (userIndex === -1) {
//     res.status(404).send({ msg: "User Not Found" });
//   }

//   req.userIndex = userIndex; //- Appended back to req
//   next();

// }

// //Here we have handled query parameter. req.query will give what we eneter query ie after ? ie ?filter=productName&value=mo; form that we get filter abd value values, then on results stored all the users array values, then if we have filters and values available then go inside if else just send  response with complete users arry ie res.send(result);, if condition match it will filter it will check for all the users array value , first it will look for first arry, user[filter] ie user[userName].included(mo), then it will return that array from users array. so here filter will loop to all the values in userd array and all tru will store in results then that will send as response. Same for product array as well.

// app.get("/api/users", (req, res) => {
//   console.log(req.query);
//   const { filter, value } = req.query;
//   console.log(filter, value);
//   let result = users;

//   if (filter && value) {
//     result = users.filter((user) => {
//       return user[filter].toLowerCase().includes(value.toLocaleLowerCase());
//     });
//   }
//   res.send(result);
// });

// app.get("/api/users/:id", (req, res) => {
//   const userID = parseInt(req.params.id);

//   if (isNaN(userID)) {
//     return res
//       .status(400)
//       .send({ msg: "Bad Request, Please check the input user id" });
//   }

//   const user = users.find((user) => user.id === userID);
//   if (user) {
//     return res.send(user);
//   }

//   res.status(404).send({ msg: "User Not Found" });
// });

// //POST Request:
// //When we send or submitting something on DB eg like submitting form we usually use post req. Here we are going to use users array to add the data , but in realtime we will create in DB.WE have to use app.use(express.json()); then only when if we want to get the req.body data we will get in json formate else will get as undefined.const newUser = {id:users[users.length-1].id +1, ...body} here will just taken the last user id and based on that we are we are inserting the new id if the last arry id is 7 our new id will be 8 then ...body here used spread operator, so if any existing json is there and our is also json it will just merage and add a one whole json else a inner json also will present.Then we are psuhing to user then we are returing response with 201 code and returing the full array. But this newUser to push we will handle with db but here we are doing with users array data.

// // app.use(express.json());
// // app.post("/api/users", (req, res) => {
// //   console.log(req.body);
// //   const { body } = req;
// //   const newUser = { id: users[users.length - 1].id + 1, ...body };
// //   console.log(newUser);
// //   users.push(newUser);
// //   console.log(users);
// //   res.status(201).send(users);
// // });

// //Validator:
// //Validator is used to validate the request data we are sending or getting(from ui) before we processing ie submitting to DB or any db operation.So first we need to insatll the express-validator, then we need to create a schema is where we will till the validation for each api. here we are writing validator for post request ie inserting user to db that request boday validation we are doing here but in same schema we can write multiple validator. I created utils folder under src and created a file called validationSchemas.mjx which means we written in plural file name so we will writing multiple validators.We used export for validator, so we use that validator in index.mjs file.syntax const validator name={filedname1 ie username:{},filedname2 ie age:{},}  - we can write multiple filedname based on the req body and we can have the fieldname. Then inside the fieldname need to write the validation ie const validator name={filedname1 ie username:{notEmpty: {errorMessage: "user name should not be empty"}},filedname2 ie age:{},} like this we can have comma seperated and have multiple validation for each field name. Refer the validator in orginal schema file.Then we need to import import { checkSchema, validationResult, matchedData } from "express-validator"; as we will be using this . The all method will take 3 argument we know the path and req handler, but inbetween we can have the checkSchema(createUserValidation) which will act as middleware its initaial place where validation take place we will pass the our created validator to here, then on the req handler const result = validationResult(req); we are passing the request, what it will do is it will compare the req with validator and return the result, if all passed then return empty error else it will return the array with all the error msg detals like which filed , location , error msg etclike this

// /*
// {
//   "error": [
//     {
//       "type": "field",
//       "value": "q",
//       "msg": "user name length must be between 3 to 12 character length",
//       "path": "userName",
//       "location": "body"
//     }
//   ]
// }*/ //Then that we are send as response as well if the validation was not successful.If we have multiple filed validationfailed all it will have it in array and will send everything. One more thing if we send the re body with only username and if our validator dosent have age , then what it will do is its only update the username alone because we use body like this ie const body = matchedData(req); the req only matched data we are sending to body. if we did not metion the field in validator even if we pass that in req that will ignore when we push to db.
// app.use(express.json());
// app.post("/api/users", checkSchema(createUserValidation),
//   (req, res) => {

//     const result = validationResult(req);
//     console.log(result);
//     if(!result.isEmpty()) {
//       return res.status(400).send({error:result.array()});
//     }
//   console.log(req.body);
//   // const { body } = req;

//   const body = matchedData(req);
//   const newUser = { id: users[users.length - 1].id + 1, ...body };
//   console.log(newUser);
//   users.push(newUser);
//   console.log(users);
//   res.status(201).send(users);
// });

// //PUT Request:
// //Put request usually to update the complete record, for eg if we want to update the user id 1 if the user has many argument like userName, age, so it will update the complete record, ie if we update the username alone also it will update the complete record ie new userName and old age, if user try to update ie for id 1 if we update the different user name , firest we are getting the index of the user id from users array then we are getting the data from body and updating here  users[userIndex] = { id: userID, ...body };. Same db handeling like post req. if (userIndex === -1) { means the index is not found so user is not found.
// app.put("/api/users/:id", (req, res) => {
//   const userID = parseInt(req.params.id);

//   if (isNaN(userID)) {
//     return res
//       .status(400)
//       .send({ msg: "Bad Request, Please check the input user id" });
//   }

//   const userIndex = users.findIndex((user) => user.id === userID);
//   if (userIndex === -1) {
//     res.status(404).send({ msg: "User Not Found" });
//   }

//   const { body } = req;
//   users[userIndex] = { id: userID, ...body };
//   return res.status(200).send(users);
// });

// //PATCH Request
// //The only change we did here is users[userIndex] = { ...users[userIndex], ...body }; so what is happ here is
// /*
// It updates an existing user by merging the old data with the new data.

// Step-by-step breakdown:
// 1. users[userIndex]

// This is the original user object you want to update.

// Example:

// users[userIndex] = {
//   id: 1,
//   name: "Dinesh",
//   age: 31
// }

// 2. { ...users[userIndex] }

// The ... (spread operator) makes a copy of the existing user.

// This prevents modifying the original object directly.

// 3. { ...body }

// body is the data the user sent in the API request (PATCH/PUT).

// Example:

// body = {
//   age: 32
// }

// 4. { ...users[userIndex], ...body }

// This merges both objects.

// If a field exists in both, the right side wins (new value overwrites old value).

// Example merge:

// {
//   id: 1,
//   name: "Dinesh",
//   age: 32   // updated!
// }

// 5. users[userIndex] = ...

// Stores the updated object back into the array.

// ✔ Final Result

// This one line:

// users[userIndex] = { ...users[userIndex], ...body };

// Means:

// “Replace the old user with a new object that contains all old fields, plus any updated fields from the request body.”
// */
// app.patch("/api/users/:id", (req, res) => {
//   const userID = parseInt(req.params.id);

//   if (isNaN(userID)) {
//     return res
//       .status(400)
//       .send({ msg: "Bad Request, Please check the input user id" });
//   }

//   const userIndex = users.findIndex((user) => user.id === userID);
//   if (userIndex === -1) {
//     res.status(404).send({ msg: "User Not Found" });
//   }

//   const { body } = req;
//   users[userIndex] = { ...users[userIndex], ...body };
//   return res.status(200).send(users);
// });

// //Delete Req:
// //The only change is  users.splice(userIndex,1);, so from userIndex to one element it will remove

// // app.patch("/api/users/:id", (req, res) => {
// //   const userID = parseInt(req.params.id);

// //   if (isNaN(userID)) {
// //     return res
// //       .status(400)
// //       .send({ msg: "Bad Request, Please check the input user id" });
// //   }

// //   const userIndex = users.findIndex((user) => user.id === userID);
// //   if (userIndex === -1) {
// //     res.status(404).send({ msg: "User Not Found" });
// //   }

// //   const { body } = req;
// //   users.splice(userIndex, 1);
// //   return res.status(200).send(users);
// // });

// //Different way of handeling middleware Step1:
// //Generally in below earlier delete example, when we send the req ie /api/users/:id until we send the response back ie res.status(200).send(users); inbetween what we commented are are we are performing in middle ie is actually a middleware, so that we created as a middleware ie a function created as ananymous fn with 3 param, req, res and next , becayse we are creating the middleware so we need next to go to next step, that middleware we have passed here even all the http methods usually take 3 param , like below we can give our middleware invetween the req param and request handeller, instead of using app.use we can handle like below. We gave middleware then we are getting the value we returned in middleware. in middleware we have appened the the return value back to req, so that we are getting like this ie const userIndex = req.userIndex; ie req.userIndex has the userindex value ie what we appended that we are getting back.Refere //Different way of handeling middleware Step2 for code and how we appended back to req.
// app.patch("/api/users/:id", getIndexByID, (req, res) => {
//   const userIndex = req.userIndex;
//   // const userID = parseInt(req.params.id);

//   // if (isNaN(userID)) {
//   //   return res
//   //     .status(400)
//   //     .send({ msg: "Bad Request, Please check the input user id" });
//   // }

//   // const userIndex = users.findIndex((user) => user.id === userID);
//   // if (userIndex === -1) {
//   //   res.status(404).send({ msg: "User Not Found" });
//   // }

//   const { body } = req;
//   users.splice(userIndex, 1);
//   return res.status(200).send(users);
// });

// app.get("/api/products", (req, res) => {
//   console.log(req.query);
//   const { filter, value } = req.query;
//   console.log(filter, value);
//   let result = products;

//   if (filter && value) {
//     result = products.filter((product) => {
//       return product[filter].toLowerCase().includes(value.toLocaleLowerCase());
//     });
//   }
//   res.send(result);
// });

// app.get("/api/products/:id", (req, res) => {
//   const productID = parseInt(req.params.id);

//   if (isNaN(productID)) {
//     return res
//       .status(400)
//       .send({ msg: "Bad Request, Please check the input product id" });
//   }

//   const product = products.find((product) => product.id === productID);
//   if (product) {
//     return res.send(product);
//   }

//   res.status(404).send({ msg: "User Not Found" });
// });

//Route course comment end here
