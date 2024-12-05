<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flight Ticket Booking</title>
    <link rel="stylesheet" href="assets/styles.css">
    <script src="https://cdn.jsdelivr.net/npm/vue@3/dist/vue.global.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
</head>
<body>
    <div id="app">
        <h1>Flight Ticket Booking</h1>
        <div>
            <h2>Create a Ticket</h2>
            <form @submit.prevent="createTicket">
                <input type="text" v-model="newTicket.source" placeholder="Source" required>
                <input type="text" v-model="newTicket.destination" placeholder="Destination" required>
                <input type="text" v-model="newTicket.passport_id" placeholder="Passport ID" required>
                <input type="datetime-local" v-model="newTicket.departure_time" required>
                <button type="submit">Book Ticket</button>
            </form>
        </div>

        <div>
            <h2>Booked Tickets</h2>
            <table>
                <thead>
                    <tr>
                        <th>Ticket ID</th>
                        <th>Source</th>
                        <th>Destination</th>
                        <th>Seat</th>
                        <th>Departure Time</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="ticket in tickets" :key="ticket.ticket_id">
                        <td>{{ ticket.ticket_id }}</td>
                        <td>{{ ticket.source }}</td>
                        <td>{{ ticket.destination }}</td>
                        <td>{{ ticket.seat }}</td>
                        <td>{{ ticket.departure_time }}</td>
                        <td><button @click="cancelTicket(ticket.ticket_id)">Cancel</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <script src="assets/app.js"></script>
</body>
</html>