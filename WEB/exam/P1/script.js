const input = prompt("Въведете дума")

let countA = 0
let countY = 0 // Ъ
let countO = 0
let countU = 0 // У
let countE = 0
let countI = 0


for (let i = 0; i < input.length; i++) {
   const currentLetter = input[i].toLocaleLowerCase()

   switch (currentLetter) {
      case 'а':
         countA++
         break;
      case 'ъ':
         countY++
         break;
      case 'о':
         countO++
         break;
      case 'у':
         countU++
         break;
      case 'е':
         countE++
         break;
      case 'и':
         countI++
         break;
      default:
         break;
   }
}

let output = `Броят на гласните букви е ${countA + countE + countI + countO + countU + countY}.\n`
if (countA > 0) {
   output += `а - ${countA}\n`
}

if (countY > 0) {
   output += `ъ - ${countY}\n`
}

if (countO > 0) {
   output += `о - ${countO}\n`
}

if (countU > 0) {
   output += `у - ${countU}\n`
}

if (countE > 0) {
   output += `е - ${countE}\n`
}

if (countI > 0) {
   output += `и - ${countI}\n`
}

alert(output)