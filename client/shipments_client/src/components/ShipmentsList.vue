<template>
    <div class="shipments_container">
        <div class="shipments_content">
            <h1>Shipments</h1>

            <div class="add_shipment">
                <form v-on:submit.prevent="submitShipment">
                    <div class="form-group">
                        <label for="description">Description</label>
                        <input class="text" id="description" v-model="description">
                    </div>
                    <div class="form-group">
                        <label for="title">Destination</label>
                        <input type="text" class="form-control" id="destination" v-model="destination">
                    </div>
                    <div class="form-group">
                        <label for="title">Due Date</label>
                        <input type="date" class="form-control" id="due_date" v-model="due_date">
                    </div>
                    <br/>
                    <div class="form-group">
                        <button type="submit">{{ isEditing ? "Edit Shipment" : "Add Shipment" }}</button>
                    </div>
                </form>
            </div>

            <ul class="shipments_list">
                <li v-for="shipment in shipments" :key="shipment.id">
                    <h2>{{ shipment.description }}</h2>
                    <h4>{{ shipment.destination }} | {{ shipment.due_date }}</h4>
                    <button @click="editShipment(shipment)">Edit</button>
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
                shipments: [],
                description: '',
                destination: '',
                due_date: '',
                id: '',
                isEditing: false
            }
        },
        methods: {
            async getData() {
                try {
                    await this.$http.get(`${API_URL}`).then(
                        response => {this.shipments = response.data}
                    )
                } catch (error) {
                    console.log(error)
                }
            },
            async submitShipment() {
                try {
                    if (!this.isEditing) {
                        await this.$http.post(`${API_URL}`, {
                            description: this.description,
                            destination: this.destination,
                            due_date: this.due_date
                        }).then(
                            response => {
                                this.shipments.push(response.data)
                                this.description = ''
                                this.destination= ''
                                this.due_date = ''
                            }
                        )
                    } else {
                        await this.$http.put(`${API_URL}${this.id}/`, {
                            description: this.description,
                            destination: this.destination,
                            due_date: this.due_date
                        }).then(
                            response => {
                                let objIndex = this.shipments.findIndex(s => s.id === this.id)
                                let tmp = this.shipments
                                tmp[objIndex] = response.data
                                this.shipments = tmp

                                this.description = ''
                                this.destination= ''
                                this.due_date = ''
                                this.id = ''
                                this.isEditing = false

                                this.getData()
                            }
                        )
                    }

                } catch (error) {
                    console.log(error)
                }
            },
            async editShipment(shipment){
                try {
                    this.isEditing = true
                    this.description = shipment.description
                    this.destination = shipment.destination
                    this.due_date = shipment.due_date
                    this.id = shipment.id
                } catch(error) {
                    console.log(error)
                }
            },
            async deleteShipment(shipment){
                let confirmation = confirm("Delete shipment?")

                if (confirmation) {
                    try {
                        await this.$http.delete(`${API_URL}${shipment.id}/`)
                        this.getData()
                    } catch(error) {
                        console.log(error)
                    }
                }
            }
        },
        created() {
            this.getData()
        }
    }
</script>