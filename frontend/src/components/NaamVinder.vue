<template>
    <main id="NaamVinder">

        <p v-if=error>
            {{errorMsg}}
        </p>

        <p v-else-if="missionAccomplished">
            Dat was de laatste, de email naar Hans is verstuurd, zelfvernietiging in 5 seconden.
        </p>

        <template v-else>
        
            <p>
                Tot nu toe hebben {{enteredCount}} surprisemakers een naam ingevuld.
            </p>
            
            <div v-if="!sent">
                <input 
                    type="text"
                    autofocus
                    placeholder="Geef aub een naam"
                    v-model="enteredname"
                    @keydown.enter="send"
                    >
                <button
                    @click="send"
                >
                    Verzenden
                </button>
            </div>

            <template v-else>
                <p v-if="success">
                    Gelukt, dankjewel!
                </p>
                <p v-else>
                    Aan het verzenden...
                </p>
            </template>

        </template>
    </main>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import API from '@/API';

@Component
export default class NaamVinder extends Vue {

    private enteredname = "";
    private sent = false;
    private success = false;

    private missionAccomplished = false;

    private enteredCount = "...";

    private error = false;
    private knownErrors = [
        "<naam_onbekend",
        "<naam_al_geweest"
    ]
    private unknownErrorMsg = "Whoeps, Dennis heeft een foutje gemaakt, stuur hem maar een appje...";
    private serverUnavailableMsg = "Server is onbereikbaar..."
    private errorMsg = "";

    private mounted() {
        this.getEnteredCount();
    }
    
    private send(clickevent: string) {

        this.sent = true;

        fetch(API.sendNaam(this.enteredname))
            .then(response => {
                
                if (response.status === 202) {
                    this.missionAccomplished = true;
                } else if (response.ok) {
                    this.success = true;
                } else {
                    this.error = true;
                    return response.json();
                }

            })
            .then(data => {
                
                // Give a nice error message if needed
                if (data) {
                    if (data.non_field_errors) {
                        const errCode = data.non_field_errors[0].split('>');
                        console.log(errCode);
                        if (this.knownErrors.includes(errCode[0])) {
                            this.errorMsg = errCode[1].slice(1);
                            return;
                        }
                    }

                    this.errorMsg = this.unknownErrorMsg;
                }

            })
            .catch(error => {
                console.error(error);
            });
    }

    private getEnteredCount() {

        fetch(API.naamCount)
            .then(response => {

                if (!response.ok) {
                    console.log(response.statusText);
                    throw new Error(response.statusText);
                }
                
                return response.text();
            })
            .then((val: string) => {
                this.enteredCount = val;
            })
            .catch(error => {

                this.error = true;
                this.errorMsg = this.serverUnavailableMsg;
                console.error(error);
            });
    }
}
</script>
<style scoped>
#NaamVinder {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
</style>