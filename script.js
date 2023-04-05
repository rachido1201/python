function plnToChfConverter(pln){
    var result = pln * 0.23;
    var message =  pln.toString() + " PLN are " + result.toString() + " CHF.";
    return message
}

console.log(plnToChfConverter(1));
console.log(plnToChfConverter(10));
console.log(plnToChfConverter(100));

function feettocentimeter(feet) {

    var result = feet *30.48;

    question = "how many feets are you ?";

    
    var message = feet.toString() + " FEET is " + result.toString() + "cm.";
    return message

}

console.log(feettocentimeter(6.9));