// Shirt class, with color attribute
class Shirt {
    constructor(color) {
        this.color = color
    }
}

// Let's ink some shirts using the color pallete on hand from colors.py:
// make a red shirt
import { red } from './colors.js'
let shirt1 = new Shirt(red)
console.log(`shirt1.color = ${shirt1.color}`)

// make a green shirt
import { green } from './colors.js'
let shirt2 = new Shirt(green)
console.log(`shirt2.color = ${shirt2.color}`)

// make a purple shirt
import { purple } from './colors.js'
let shirt3 = new Shirt(purple)
console.log(`shirt3.color = ${shirt3.color}`)

// But what happens if we try to ink a shirt with beige, which is not in the colors.js pallete? JS modules provide 'export default' to handle this situation.
// make a beige shirt... 
import { default as beige } from './colors.js' // shorthand is `import beige from './colors.js'` ... note lack of curly braces
let shirt4 = new Shirt(beige)
console.log(`shirt4.color = ${shirt4.color}`)