const express = require('express')
var fs = require('fs'); 
const app = express()
const port = 3000

/*app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))*/

'use strict'
/**html*/
app.get('/blue', function(req,res){

  res.send('the color blue')

})

app.get('/test.html', function(req,res){

  res.sendFile('/home/david/game/game/test.html');

})

app.get('/index.html', function(req,res) 
  {
    res.sendFile('/home/david/game/game/index.html');
  })

app.get('/recall.html', function(req,res) 
  {
    res.sendFile('/home/david/game/game/recall.html');
  })

app.get('/game.html', function (req, res) {
    res.send('game.html')
  })

  /** javascript */

  app.get('/js/span.js', function(req,res) 
  {
    res.sendFile('/home/david/game/game/js/span.js');
  })
  app.get('/js/populate.js', function(req,res) 
  {
    res.sendFile('/home/david/game/game/js/populate.js');
  })
  app.get('/js/events.js', function(req,res) 
  {
    res.sendFile('/home/david/game/game/js/events.js');
  })

  app.get('/js/static.js', function(req,res) 
  {
    res.sendFile('/home/david/game/game/js/static.js');
  })
  
  app.get('/js/scratchpad.js', function(req,res) 
  {
    res.sendFile('/home/david/game/game/js/scratchpad.js');
  })

  

/** JSON */

  app.get('/recall/readJSON.json', function(req,res) 
  {
    res.sendFile('/home/david/game/game/readJSON.json');
  })

  app.get('/recall/memory.json', function(req,res) 
  {
    res.sendFile('/home/david/game/game/memory.json');
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
