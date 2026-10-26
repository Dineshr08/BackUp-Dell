/*
//Express JS

const exp = require('express');
const app = exp();
app.listen(3000);
app.get('/', (req, res)=>{
  res.sendFile('./pages/index.html', {root:__dirname});
})

app.get('/home', (req, res)=>{
  res.redirect('./pages/index.html', {root:__dirname});
})

app.get('/contact', (req, res)=>{
  res.sendFile('./pages/contact.html', {root:__dirname});
})

app.get('/about', (req, res)=>{
  res.sendFile('./pages/about.html', {root:__dirname});
})

app.use((req, res)=>{
  res.sendFile('./pages/notFound.html', {root: __dirname});
})
  */

//Middleware

const exp = require('express');
const morgan = require('morgan');
const app = exp();
app.listen(3000);

app.get('/', (req, res)=>{
  res.sendFile('./pages/index.html', {root:__dirname});
})

app.get('/home', (req, res)=>{
  res.redirect('./pages/index.html', {root:__dirname});
})

app.use(morgan('dev'));

app.use((req, res, next)=>{
  console.log('Middleware1');
  next();
})

app.get('/contact', (req, res)=>{
  res.sendFile('./pages/contact.html', {root:__dirname});
})

app.get('/about', (req, res)=>{
  res.sendFile('./pages/about.html', {root:__dirname});
})

app.use((req, res, next)=>{
  console.log('Middleware2');
  next();
})


app.use((req, res)=>{
  res.sendFile('./pages/notFound.html', {root: __dirname});
})