// Bring in the DB connection and the Room schema
const Mongoose = require('./db');
const Room = require('./GSWA');

// Read seed data from json file
var fs = require('fs');
var rooms = JSON.parse(fs.readFileSync('./data/roomTest.json', 'utf8'));

// delete any existing records, then insert seed data
const seedDB = async () => {
    await Room.deleteMany({});
    await Room.insertMany(rooms);
};

// Close the MongoDB connection and exit
seedDB().then(async () => {
    await Mongoose.connection.close();
    process.exit(0);
});