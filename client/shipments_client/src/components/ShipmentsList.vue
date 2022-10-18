<template>
    <div class="shipments_container">
        <div class="shipments_content">
            <h1>Shipments List</h1>
            <ul class="shipments_list">
                <li v-for="shipment in shipments" :key="shipment.id">
                    <h2>{{ shipment.description }}</h2>
                    <p>{{ shipment.destination }}</p>
                    <p>{{ shipment.due_date }}</p>
                    <button @click="deleteShipment(shipment)">Delete</button>
                </li>
            </ul>
        </div>
    </div>
</template>


<script>
    const API_URL = 'http://localhost:8000/api/shipments/'
    export default {
        data() {
            return {
                shipments: []
            }
        },
        methods: {
            async getData() {
                try {
                    await this.$http.get(`${API_URL}`).then(
                        response => {this.shipments = response.data}
                    )
                } catch (error) {
                    console.log(error);
                }
            },
        },
        created() {
            this.getData();
        }
    }
</script>