let age = 17
if(age <= 18 && age<= 16){
    let b = 12
    console.log("data")
}else{
    console.log("not data")
}

const str = "kamal"
console.log(str.length)

let reversed = []

for(i=str.length-1; i>=0; i--){
    reversed.push(str[i])
}
console.log([reversed.join('')])

const data = [0,1,2,3,[4,5,[6,7,8,[9]]]]
console.log(data.flat(3))
let pushedArr

// for(let i=0; i<data.length; i++){
//     if(Array.isArray){
//         console.log("data",data[i])
//     }else{
//         pushedArr.push("not data",data[i])
//     }

// }
for(let item of data){
    let result = []
    if(Array.isArray(item)){
        result = result.concat(flattenArr(item))
    }else{
        result.push(item)
    }
}



