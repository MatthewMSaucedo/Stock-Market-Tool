const express = require("express");

const router = express.Router();

router.get("/ROE", (req, res, next) => {

    var spawn = require("child_process").spawn; 
    var process = spawn('python', ["../../financial-logic/test.py", req.body.netIncome, req.body.shareholderEquity]); 
    
    process.stdout.on('data', function(data) { 
        res.send(data.toString()); 
    } ) 
  
});

router.get("/IntrinsicValue", (req, res, next) => {

    var spawn = require("child_process").spawn; 
    var process = spawn('python', ["../../Financial-Logic/test.py", req.query.ticker]); 
    
    process.stdout.on('data', function(data) { 
        res.send(data.toString()); 
    } ) 
  
});

module.exports = router;
