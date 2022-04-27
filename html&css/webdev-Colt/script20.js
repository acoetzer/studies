function multiply (num1, num2) {
    return num1 * num2;
}

function isShortsWeather (temp) {
    if (temp >= 75) {
        return true;
    } else {
        return false;
    }
}

function lastElement (arr) {
    if (arr.length > 0) {
        return arr[arr.length - 1];
    } else {
        return null;
    }
}

function capitalize (str) {
    return str[0].toUpperCase() + str.slice(1);
}

function sumArray (arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        // sum = sum + arr[i];
        sum += arr[i];
    }
    return sum;
}

function returnDay (num) {
    const dow = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
    
    if (num < 1 || num > 7) {
        return null;
    }
    return dow[num - 1]
}