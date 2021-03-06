const express = require("express");
const bcryptjs = require("bcryptjs");
const jwt = require("jsonwebtoken");
const User = require("../models/user");
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

const router = express.Router();

function getCurrentPrice(ticker, callback) {
    const Http = new XMLHttpRequest();
    const url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '&apikey=6HYZSQEHOQOURB6Y';
    Http.open("GET", url, true);
    Http.send();

    Http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          var myObj = JSON.parse(this.responseText);
          if(myObj.hasOwnProperty('Error Message')) {
              callback.apply(-1);
              return;
          }
          callback.apply(parseFloat(myObj["Global Quote"]["05. price"]));
        }
    };
}

/*
var getCurrentPrice = function(ticker) {
    return new Promise(function(resolve, reject) {
        const Http = new XMLHttpRequest();
        const url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '&apikey=OjdkMzliY2VkOWVlYTZjYjNlYzg2NDkxZDBmMzVjZTdi';
        Http.open("GET", url, true);
        Http.send();

        Http.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
            var myObj = JSON.parse(this.responseText);
            if(myObj.hasOwnProperty('Error Message')) {
                reject(Error("It broke"));
            }
            resolve(parseFloat(myObj["Global Quote"]["05. price"]));
            }
        };
    });
  }
*/

router.post("/register", (req, res, next) => {
    bcryptjs.hash(req.body.password, 10)
        .then(hash => {
            console.log(req.body);
            const user = new User({
                email: req.body.email,
                username: req.body.username,
                password: hash
            });
            user.save()
                .then(result => {
                    res.status(201).json({
                       message: 'User Created!',
                       result: result
                    });
                })
                .catch(err => {
                    console.log(err);
                    res.status(500).json({
                        error: err
                    });
                });
        });
});

router.post("/login", (req, res, next) => {
    let fetchedUser;
    User.findOne({username: req.body.username})
        .then(user => {
            if(!user)
            {
                return res.status(401).json({
                    message: "User does not exist!"
                });
            }
            fetchedUser = user;
            return bcryptjs.compare(req.body.password, user.password);
        })
        .then(result => {
            if(!result)
            {
                return res.status(401).json({
                    message: "User authentication failed!"
                });
            }
            const token = jwt.sign({ username: fetchedUser.username, userId: fetchedUser._id}, 'this_serves_as_a_long_string',
            { expiresIn: '1h'});
            res.status(200).json({
                token: token
            });
        })
        .catch(err => {
            return res.status(401).json({
                message: "User authentication failed!"
            });
        });
});

router.post("/addWatchlistTicker", (req, res, next) => {
    User.findOne({username: req.body.username})
        .then(user => {
            if(!user)
            {
                return res.status(401).json({
                    message: "User does not exist!"
                });
            }
            if(!user.stocks.some(stock => stock.ticker == req.body.ticker))
            {
                var today = new Date();
                var currentDate = today.getMonth() + '/' + today.getDate() + '/' + today.getFullYear();
                getCurrentPrice(req.body.ticker, function(){
                    var price = this;
                    if(price == -1){
                        return res.status(500).json({
                            message: "Unable to obtain price data for the ticker entered!"
                        });
                    }
                    const newStock = {
                        ticker: req.body.ticker,
                        dateAdded: currentDate,
                        priceEntered: price,
                        currentPrice: 0
                    };
                    user.stocks.push(newStock);
                    user.save().then(result => {
                        res.status(201).json({
                           message: 'Ticker added to watchlist!',
                           result: result
                        });
                    })
                    .catch(err => {
                        res.status(500).json({
                            error: err
                        });
                    });
                });
            }
            else {
                res.status(201).json({
                    message: 'Ticker is already in watchlist!'
                 });
            }
        })
});

router.post("/removeWatchlistTicker", (req, res, next) => {
    User.findOne({username: req.body.username})
        .then(user => {
            if(!user)
            {
                return res.status(401).json({
                    message: "User does not exist!"
                });
            }
            if(user.stocks.some(stock => stock.ticker == req.body.ticker))
            {
                var index = user.stocks.findIndex(stock => stock.ticker == req.body.ticker);
                user.stocks.splice(index, 1);
                user.save().then(result => {
                    res.status(201).json({
                       message: 'Ticker removed from watchlist!',
                       result: result
                    });
                })
                .catch(err => {
                    res.status(500).json({
                        error: err
                    });
                });
            }
            else {
                res.status(201).json({
                    message: 'Ticker did not exist in watchlist!'
                 });
            }
        })
});

router.post("/getWatchlist", (req, res, next) => {
    User.findOne({username: req.body.username})
        .then(user => {
            if(!user)
            {
                return res.status(401).json({
                    message: "User does not exist!"
                });
            }
            else {
                var i = 0;
                var counter = 0;
                for(i = 0; i < user.stocks.length; i++)
                {            
                    getCurrentPrice(user.stocks[i]["ticker"], function(){
                        var price = this;
                        if(price == -1){
                            return res.status(500).json({
                                message: "Unable to obtain price data for the ticker entered!"
                            });
                        }

                        user.stocks[counter]["currentPrice"] = price;
                        counter++;
                        if(counter == user.stocks.length)
                        {
                            return res.status(201).json(user.stocks);
                        }
                    });
                }
            }
        })
});

module.exports = router;
