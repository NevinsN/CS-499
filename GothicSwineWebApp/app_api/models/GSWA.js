const mongoose = require('mongoose');

// Define test schema
const roomSchema = new mongoose.Schema({
    name: {type: String, required: true, index: true},
    description: {type: String, required: true}
});

const Room = mongoose.model('rooms', roomSchema);
module.exports = Room;