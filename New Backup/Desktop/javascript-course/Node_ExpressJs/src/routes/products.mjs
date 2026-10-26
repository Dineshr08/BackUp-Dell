import { Router } from "express";
import { products } from "../utils/constants.mjs";

const router = Router();


router.get("/api/products", (req, res) => {
  req.session.visited = true;
  console.log(req.session.id);
  console.log(req.query);
  const { filter, value } = req.query;
  console.log(filter, value);
  let result = products;

  if (filter && value) {
    result = products.filter((product) => {
      return product[filter].toLowerCase().includes(value.toLocaleLowerCase());
    });
  }
  res.send(result);
});

router.get("/api/products/:id", (req, res) => {
  const productID = parseInt(req.params.id);

  if (isNaN(productID)) {
    return res
      .status(400)
      .send({ msg: "Bad Request, Please check the input product id" });
  }

  const product = products.find((product) => product.id === productID);
  if (product) {
    return res.send(product);
  }

  res.status(404).send({ msg: "User Not Found" });
});

export default router;