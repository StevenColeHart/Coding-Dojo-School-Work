function fizzBuzz(number){
    var output = [];
    if (isNaN(number) || number < 0){
        return ("must be a positive number");
    }
    for(i = 1; i <= number; i++){
        if(i % 3 == 0 && i % 5 == 0){
            output.push("FizzBuzz");
        }
        else if (i % 3 == 0){
            output.push("Fizz");
        }
        else if (i % 5 == 0){
            output.push("Buzz");
        }
        else (output.push(i))
    }
    output.toString()
    return output

}

document.write(fizzBuzz(27))