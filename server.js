/* Setting things up. */
var path = require('path'),
    fs = require("fs"),
    express = require('express'),
    app = express(),
    Twit = require('twit'),
    config = {
    /* Be sure to update the .env file with your API keys. See how to get them: https://botwiki.org/tutorials/how-to-create-a-twitter-app */
      twitter: {
        consumer_key: process.env.CONSUMER_KEY,
        consumer_secret: process.env.CONSUMER_SECRET,
        access_token: process.env.ACCESS_TOKEN,
        access_token_secret: process.env.ACCESS_TOKEN_SECRET
      }
    },
    T = new Twit(config.twitter);

app.use(express.static('public'));

/* You can use uptimerobot.com or a similar site to hit your /BOT_ENDPOINT to wake up your app and make your Twitter bot tweet. */


app.all("/" + process.env.BOT_ENDPOINT, function (request, response) {
/* The example below tweets out "Hello world!". */
  var resp = response;

/*create mytweet*/
var mytweet = "The next big thing is: ";
var X = "";
var Y = "";

fs.readFile("X.txt", 'utf8', function(err, data){
    if(err) throw err;
    var stringdata = data +"";
    var lines = stringdata.split('\n');

  X = lines[Math.floor(Math.random()*lines.length)];

  fs.readFile("Y.txt", function(err, data){
    if(err) throw err;
    var stringdata = data + "";
    var lines = stringdata.split('\n');
    console.log(lines);

  Y = lines[Math.floor(Math.random()*lines.length)];

    mytweet += X;
mytweet += " but for ";


  console.log("y is: " + Y);
  mytweet += Y;
  console.log("my tweet: " + mytweet);


  T.post('statuses/update', {


    status: mytweet



  }, function(err, data, response) {
    if (err){
      resp.sendStatus(500);
      console.log('Error!');
      console.log(err);
    }
    else{
      resp.sendStatus(200);
    }
  });

  });
});

});

var listener = app.listen(process.env.PORT, function () {
  console.log('Your bot is running on port ' + listener.address().port);
});
