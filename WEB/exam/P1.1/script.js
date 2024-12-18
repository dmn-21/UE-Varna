const input = prompt("Въведете дума: ")

let a = 0;
let y = 0;
let o = 0;
let u = 0;
let e = 0;
let i = 0; 
 

for (let ii = 0; ii < input.length; ii++) {
    let curr = input[ii].toLocaleLowerCase()
    if (curr == 'а') a++;
    if (curr == 'ъ') y++;
    if (curr == 'о') o++;
    if (curr == 'у') u++;
    if (curr == 'е') e++;
    if (curr == 'и') i++;
}

alert(`Броят на гласните букви е ${a+y+o+u+e+i}`)

if (a > 0) alert(`а-${a}`);
if (y > 0) alert(`ъ-${y}`);
if (o > 0) alert(`о-${o}`);
if (u > 0) alert(`у-${u}`);
if (e > 0) alert(`е-${e}`);
if (i > 0) alert(`и-${i}`);