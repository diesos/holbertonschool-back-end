# <p align = "center">📜 ES6 - Classes</p>
## <p align="center">🎓 Holberton School Program - Lille</p>

<img src="https://i.imgur.com/SYkTyAA.png" width="100%" />

### Learning Objectives
- How to define a Class
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols

### Tasks
- **0-classroom.js** : implement a class named `ClassRoom`, Prototype: `export default class ClassRoom`. It should accept one attribute named `maxStudentsSize` (Number) and assigned to `_maxStudentsSize`
- **1-make_classrooms.js** : import the `ClassRoom` class from `0-classroom.js`, implement a function named `initializeRooms`. It should return an array of 3 `ClassRoom` objects with the sizes 19, 20, and 34 (in this order)
- **2-hbtn_course.js** : implement a class named `HolbertonCourse`
- **3-currency.js** : implement a class named `Currency`
- **4-pricing.js** : import the class `Currency` from `3-currency.js`, implement a class named `Pricing`
- **5-building.js** : implement a class named `Building`
- **6-sky_high.js** : import `Building` from `5-building.js`, implement a class named `SkyHighBuilding` that extends from `Building`
- **7-airport.js** : implement a class named `Airport`
- **8-hbtn_class.js** : implement a class named `HolbertonClass`
- **9-hoisting.js** : fix this code and make it work
<details>
<summary>Code to fix</summary>

```javascript
const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  get year() {
    return this._year;
  }

  get location() {
    return this._location;
  }
}

const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

export class StudentHolberton {
  constructor(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get holbertonClass() {
    return this.holbertonClass;
  }

  get fullStudentDescription() {
    return `${self._firstName} ${self._lastName} - ${self._holbertonClass.year} - ${self._holbertonClass.location}`;
  }
}


export const listOfStudents = [student1, student2, student3, student4, student5];
```
</details>

- **10-car.js** : implement a class named `Car`
