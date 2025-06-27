/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
use('20250619lab');

// Step 1: Insert students.
// db.getCollection('students').insertMany([
//     { "name": "Carl", "age": 21, "courses": [{ "name": "Math", "grade": "A" }, { "name": "History", "grade": "B" }] },
//     { "name": "Max", "age": 23, "courses": [{ "name": "English", "grade": "D" }, { "name": "History", "grade": "C" }] },
//     { "name": "Jenny", "age": 22, "courses": [{ "name": "Chemistry", "grade": "B" }, { "name": "History", "grade": "A" }] },
//     { "name": "Artur", "age": 24, "courses": [{ "name": "Politics", "grade": "B" }, { "name": "Swedish", "grade": "B" }] },
//     { "name": "Ted", "age": 22, "courses": [{ "name": "History", "grade": "D" }, { "name": "Biology", "grade": "A" }] },
//     { "name": "Christina", "age": 21, "courses": [{ "name": "Math", "grade": "A" }, { "name": "Physics", "grade": "A" }] },
//     { "name": "Bruno", "age": 25, "courses": [{ "name": "History", "grade": "B" }, { "name": "Spanish", "grade": "B" }] },
//     { "name": "Noah", "age": 22, "courses": [{ "name": "Politics", "grade": "B" }, { "name": "German", "grade": "C" }] },
//     { "name": "Nellie", "age": 21, "courses": [{ "name": "History", "grade": "B" }, { "name": "Geography", "grade": "B" }] },
//     { "name": "Sofia", "age": 23, "courses": [{ "name": "History", "grade": "D" }, { "name": "Math", "grade": "D" }] },
//     { "name": "Eric", "age": 24, "courses": [{ "name": "Chemistry", "grade": "C" }, { "name": "Physics", "grade": "B" }] },
//     { "name": "Hugo", "age": 25, "courses": [{ "name": "English", "grade": "D" }, { "name": "Biology", "grade": "C" }] }
// ]);


// Step 2: Query All students.
db.students.find({});


// // Step 3: Query on student by Name.
// db.students.findOne({ "name": "Carl" });
// db.students.findOne({ "name": "Xiaomei" });


// // Step 4: Find students that are older Than 21 for example.
// db.students.find({ age: { $gt: 21 } });


// // Step 5: Add a Course to Max.
// db.students.updateOne(
//     { "name": "Max" },
//     {
//         "$push": {
//             "courses": { "name": "Math", "grade": "E" }
//         }
//     }
// )


// // Step 6: Update Carls course to Physics.
// db.students.updateOne({ "name": "Carl" }, { $set: { "courses": [{ "name": "Physics", "grade": "A" }] } })



// Step 7: Delete Jenny
// db.students.deleteOne({ "name": "Jenny" })


// Bonus1: List all students enrolled in Math for example or any other course.
// db.students.find({ "name": $in: ["Math"] });





// Bonus2: Count how many students are enrolled in at least 1 course.
// db.students.aggregate({$group:"courses":})
































// Run a find command to view items sold on April 4th, 2014.
// const salesOnApril4th = db.getCollection('sales').find({
//     date: { $gte: new Date('2014-04-04'), $lt: new Date('2014-04-05') }
// }).count();

// // Print a message to the output window.
// console.log(`${salesOnApril4th} sales occurred in 2014.`);

// // Here we run an aggregation and open a cursor to the results.
// // Use '.toArray()' to exhaust the cursor to return the whole result set.
// // You can use '.hasNext()/.next()' to iterate through the cursor page by page.
// db.getCollection('sales').aggregate([
//     // Find all of the sales that occurred in 2014.
//     { $match: { date: { $gte: new Date('2014-01-01'), $lt: new Date('2015-01-01') } } },
//     // Group the total sales for each product.
//     { $group: { _id: '$item', totalSaleAmount: { $sum: { $multiply: ['$price', '$quantity'] } } } }
// ]);
