const express = require('express')
var fs = require('fs'); 
var path = require('path');
const app = express()
const port = 3000

/*app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))*/

'use strict'
/**html*/
app.get('/blue', function(req,res){

  res.send('the color blue' + __dirname + '/test.html')

})

app.get('/test.html', function(req,res){
  
  res.sendFile(path.join(__dirname + '/test.html'));

})

app.get('/index.html', function(req,res) 
  {
    res.sendFile(path.join(__dirname + '/index.html'));
  })

app.get('/recall.html', function(req,res) 
  {
    res.sendFile(path.join(__dirname + '/recall.html'));
  })

app.get('/game.html', function (req, res) {

    res.sendFile(path.join(__dirname + '/game.html'));

  })

  /** javascript */

  app.get('/js/span.js', function(req,res) 
  {
    res.sendFile(path.join(__dirname,'/span.js'));
    
  })
  app.get('/js/populate.js', function(req,res) 
  {
    res.sendFile(path.join(__dirname,'/populate.js'));
  })
  app.get('/js/events.js', function(req,res) 
  {
    res.sendFile(path.join(__dirname,'/events.js'));
  })

  app.get('/js/static.js', function(req,res) 
  {
    res.sendFile(path.join(__dirname,'/static.js'));
  })
  
  app.get('/js/scratchpad.js', function(req,res) 
  {
    res.sendFile(path.join(__dirname,'/scratchpad.js'));
  })

  

/** JSON */

  app.get('/recall/readJSON.json', function(req,res) 
  {
    res.sendFile(path.join(__dirname,'/readJSON.json'));
  })

  app.get('/recall/memory.json', function(req,res) 
  {
    res.sendFile(path.join(__dirname,'/memory.json'));
  })

 /* TEST AREA */ 

app.get('/save/:data', function (req, res) {
    
    var lyrics = JSON.stringify(req.params);

    fs.appendFile('database.txt', lyrics, (err) => {
        if(err) throw err;

    })
    res.send(req.params)
  })


  
app.listen(port, () => console.log(`Example app listening on port ${port}!`))
