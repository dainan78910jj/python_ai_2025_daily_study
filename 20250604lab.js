console.log("Problem 1: Rectangle");

class Rectangle {
    constructor(width, height, color) {
        if (width > 0 && height > 0 && color.length > 0) {
            this.width = width;
            this.height = height;
            this.color = color;
        } else {
            this.width = 0;
            this.height = 0;
            this.color = "unknown";
        }
    }

    calcArea() {
        return this.width * this.height;
    }
}

let rect = new Rectangle(4, 5, "red");
console.log(rect.width);
console.log(rect.height);
console.log(rect.color);
console.log(rect.calcArea());

console.log("Problem 2: Person");

class Person {
    constructor(firstname, lastname, age, email) {

        if (firstname.length > 0 && lastname.length > 0 && age > 0) {
            this.firstname = firstname;
            this.lastname = lastname;
            this.age = age;
            this.email = email;
        }
        // String(email)
        //     .toLowerCase()
        //     .match(
        //         /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        //     );


    }

    toString() {
        return `${this.firstname} ${this.lastname} (age: ${this.age}, email: ${this.email})`
    }
}

let person = new Person("Maria", "Petterson", 22, "mp@gmail.com");
console.log(person.toString())

console.log("Problem 3: Get Persons");
const getPersonsInfo = () => {
    return [new Person("Maria", "Petterson", 22, "mp@gmail.com"), new Person("Lexicon"), new Person("Stefan", "Larsson", 25), new Person("Peter", "Jansson", 24, "ptr@live.com")]
}
console.log(getPersonsInfo);

console.log("Problem 4: Circle");
class Circle {
    constructor(radius) {
        this.radius = radius;
    }

    get diameter() {
        return this.radius * 2;
    }

    set diameter(value) {
        this.radius = value / 2;
    }

    area() {
        let pi = 3.14159265359;
        return (pi * this.radius * this.radius);
    }
}

let c = new Circle(2);
console.log(`Radius: ${c.radius}`);
console.log(`Diameter: ${c.diameter}`);
console.log(`Area: ${c.area()}`);

c.diameter = 1.6;
console.log(`Radius: ${c.radius}`);
console.log(`Diameter: ${c.diameter}`);
console.log(`Area: ${c.area()}`);



console.log("Problem 5: Point Distance");

class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    static distance(input1, input2) {

        const lengthOfXaxis = Math.abs(input1.x - input2.x);
        const lengthOfYaxis = Math.abs(input1.y - input2.y);

        const resultOfDistance = Math.sqrt(lengthOfXaxis * lengthOfXaxis + lengthOfYaxis * lengthOfYaxis);

        return resultOfDistance;
    }
}

let p1 = new Point(5, 5);
let p2 = new Point(9, 8);

console.log(Point.distance(p1, p2));