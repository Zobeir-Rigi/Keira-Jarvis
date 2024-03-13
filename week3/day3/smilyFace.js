// let smileCount = 0 ;
// let smileFace = ":)"

// while ( smileCount < 10 ){
//     console.log (smileFace)
//     smileCount++
//     smileFace += ")"
// }
const smileFace = [":)"];
let smileCount = 0;

while (smileCount < 10) {
    console.log(smileFace.join(''));
    smileFace.push(")");

    smileCount++;
}
