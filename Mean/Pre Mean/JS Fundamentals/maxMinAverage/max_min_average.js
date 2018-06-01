
function maxMinAvg(arr){
    var max = 0
    var min = 0
    var total = 0
    for (i = 0; i < arr.length; i ++){
        if( max < arr[i]){
            max = arr[i]
        }
        if (min > arr[i]){
            min = arr[i]
        }
        total += arr[i]
    }
    var avg = (total/arr.length)

    return("your minimum is: "+min+" your maximum is: "+max+" and your average is "+avg)
}
arrOne = [45,67,1000,-93.8, 3, 14, -57];

document.write(maxMinAvg(arrOne))
