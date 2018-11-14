const express = require('express')
var fs = require('fs'); 
const app = express()
const port = 3000

/*app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))*/

'use strict'


  
app.get('/recall.html', function(req,res) 
  {
    res.sendFile('/home/david/game/game/recall.html');
  })


  app.get('/recall/readJSON.json', function(req,res) 
  {
    res.sendFile('/home/david/game/game/readJSON.json');
  })


  app.get('/recall/memory.json', function(req,res) 
  {
    res.sendFile('/home/david/game/game/memory.json');
  })




app.get('/save/:data', function (req, res) {
    
    var lyrics = JSON.stringify(req.params);

    fs.appendFile('database.txt', lyrics, (err) => {
        if(err) throw err;

    })
    res.send(req.params)
  })


app.use(express.static('/'))

/*app.get('/game.html', function (req, res) {
    res.send('game.html')
  })*/
  
app.listen(port, () => console.log(`Example app listening on port ${port}!`))
