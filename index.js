const express = require('express')
var fs = require('fs'); 
const app = express()
const port = 3000

/*app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))*/

'use strict'


  
app.get('/', function(req,res) 
  {
    res.sendFile('/home/david/Documents/game/game/game.html');
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
