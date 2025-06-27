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
use('20250623lab');

// Step 1: Insert teachers.
// db.getCollection("teachers").insertMany([
//     { "name": "Anna Svensson", "department": "natural_sciences", "courses": ["Math", "Physics"] },
//     { "name": "Eva Johansson", "department": "Languages", "courses": ["English", "Swedish"] },
//     { "name": "Fredrik Lundberg", "department": "natural_sciences", "courses": ["Chemistry", "Math"] },
//     { "name": "Sara Ekman", "department": "Languages", "courses": ["German", "Swedish"] },
//     { "name": "Kevin Hansson", "department": "natural_sciences", "courses": ["Biology", "Physics"] },
//     { "name": "Hans Lindstrom", "department": "natural_sciences", "courses": ["Biology", "Chemistry"] },
//     { "name": "Johan Eriksson", "department": "social_sciences", "courses": ["History", "Geography"] },
//     { "name": "Moa Martinson", "department": "social_sciences", "courses": ["History", "Politics"] },
//     { "name": "Linda Persson", "department": "social_sciences", "courses": ["Geography", "Politics"] },
//     { "name": "Ellinor Axner", "department": "Languages", "courses": ["English", "Spanish"] },
// ])

// // Step 2: Query all teachers.
// db.teachers.find({});


// // Step 3: Insert students.
db.getCollection('students').insertMany([
    { "name": "Carl", "age": 21, "grade_history": [{ "course": "Math", "grades": ["A", "B"] }, { "course": "History", "grades": ["A", "C"] }] },
    { "name": "Max", "age": 23, "grade_history": [{ "course": "English", "grades": ["D", "B"] }, { "course": "History", "grades": ["B", "C"] }] },
    { "name": "Jenny", "age": 22, "grade_history": [{ "course": "Chemistry", "grades": ["A", "C"] }, { "course": "History", "grades": ["D", "C"] }] },
    { "name": "Artur", "age": 24, "grade_history": [{ "course": "Politics", "grades": ["B"] }, { "course": "Swedish", "grades": ["B"] }, { "course": "History", "grades": ["D", "E"] }] },
    { "name": "Ted", "age": 22, "grade_history": [{ "course": "History", "grades": ["D", "D"] }, { "course": "Biology", "grades": ["A", "B"] }] },
    { "name": "Christina", "age": 21, "grade_history": [{ "course": "Math", "grades": ["A", "A"] }, { "course": "Physics", "grades": ["B", "A"] }, { "course": "History", "grades": ["A", "B"] }] },
    { "name": "Bruno", "age": 25, "grade_history": [{ "course": "History", "grades": ["B", "C"] }, { "course": "Spanish", "grades": ["B"] }, { "course": "Math", "grades": ["C", "C"] }] },
    { "name": "Noah", "age": 22, "grade_history": [{ "course": "Politics", "grades": ["B", "C"] }, { "course": "German", "grades": ["C", "B"] }, { "course": "History", "grades": ["A", "C"] }] },
    { "name": "Nellie", "age": 21, "grade_history": [{ "course": "History", "grades": ["B"] }, { "course": "Geography", "grades": ["D", "B"] }] },
    { "name": "Sofia", "age": 23, "grade_history": [{ "course": "History", "grades": ["C", "D"] }, { "course": "Math", "grades": ["D"] }] },
    { "name": "Eric", "age": 24, "grade_history": [{ "course": "Chemistry", "grades": ["C", "B"] }, { "course": "Physics", "grades": ["B", "C"] }, { "course": "History", "grades": ["B", "C"] }] },
    { "name": "Hugo", "age": 25, "grade_history": [{ "course": "English", "grades": ["D", "C"] }, { "course": "Biology", "grades": ["C", "E"] }, { "course": "History", "grades": ["E", "C"] }] }
]);

// // Step 4: Query all students.
db.students.find({});

// Part 2, question 1: Find all students who have taken the course "Physics" and received an "A" in (either courses or grade_history).
// db.students.find({ 'grade_history': { "$elemMatch": { "course": "Physics" } } });
// db.students.find({ 'grade_history': { "$elemMatch": { "grades": { "$all": ['A'] } } } });
// db.students.find({
//     'grade_history': {
//         '$all': [
//             {
//                 "$elemMatch": {
//                     "course": "Physics"
//                 }
//             },
//             {
//                 "$elemMatch": {
//                     "grades": {
//                         "$all": ['A']
//                     }
//                 }
//             }
//         ]
//     }
// });

// Part 2 question 2: Find all teachers who teach a course where at least one student has an "A".

const coursesWithA = db.students.aggregate([
    { $unwind: "$grade_history" },
    { $match: { "grade_history.grades": "A" } },
    { $group: { _id: null, courses: { $addToSet: "$grade_history.course" } } }
]).toArray()[0]?.courses || [];

db.teachers.find({ courses: { $in: coursesWithA } });




// // Part 2 question 3: Add a new course to one of the students ( eg "Programming", grade: "B"). Make sure to update both courses and grade_history.
// db.students.updateOne(
//     { "name": "Christina" },
//     {
//         "$push": {
//             "grade_history": { "course": "Programming", "grade": ["B"] }
//         }
//     }
// )
// db.students.find({ "name": "Christina" });



// Part 2 question 4: Delete all students who are not enrolled in any course (courses array is empty or missing).
// db.students.insertOne({ "name": "Amanda", "age": 26, "grade_history": [] })

// db.students.deleteOne({ 'grade_history.0': { '$exists': false } })

// db.students.find({ "name": "Amanda" });