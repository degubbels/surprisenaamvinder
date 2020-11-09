
const API_BASE_URL = "https://surprisenaamvinder.herokuapp.com/api/";

export default class API {

    public static get naamCount() {
        return new Request (API_BASE_URL + 'naamcount/');
    }

    public static sendNaam(naam: string) {
        return new Request(
            API_BASE_URL + 'naam/', {
                method: 'POST',
                body: JSON.stringify({
                    'naam': naam
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            }
        )
    }
}