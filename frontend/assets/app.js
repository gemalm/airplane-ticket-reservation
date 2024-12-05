const app = Vue.createApp({
    data() {
        return {
            tickets: [],
            newTicket: {
                source: '',
                destination: '',
                passport_id: '',
                departure_time: ''
            }
        };
    },
    methods: {
        async fetchTickets() {
            try {
                const response = await axios.get('http://localhost:5001/tickets');
                this.tickets = response.data;
            } catch (error) {
                console.error('Error fetching tickets:', error);
            }
        },
        async createTicket() {
            try {
                const response = await axios.post('http://localhost:5001/tickets', this.newTicket);
                this.tickets.push(response.data);
                this.newTicket = { source: '', destination: '', passport_id: '', departure_time: '' };
            } catch (error) {
                console.error('Error creating ticket:', error);
            }
        },
        async cancelTicket(ticket_id) {
            try {
                await axios.delete(`http://localhost:5001/tickets/${ticket_id}`);
                this.tickets = this.tickets.filter(ticket => ticket.ticket_id !== ticket_id);
            } catch (error) {
                console.error('Error canceling ticket:', error);
            }
        }
    },
    mounted() {
        this.fetchTickets();
    }
});

app.mount('#app');