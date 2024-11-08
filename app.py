from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Mock database to store COVID-19 data and hospital resources
covid_data = {
    "global": {"cases": 1000000, "deaths": 50000, "recovered": 900000},
}
vaccination_data = {"doses_given": 5000000, "percent_vaccinated": 70}
hospital_resources = {"beds": 200, "ventilators": 50, "icu_capacity": 80}


# Endpoint to retrieve current COVID-19 cases by region
@app.route('/covid/cases', methods=['GET'])
def get_covid_cases():
    region = request.args.get('region', 'global')
    data = covid_data.get(region, covid_data['global'])
    return jsonify(data)


# Endpoint to retrieve detailed COVID-19 statistics for a specific region
@app.route('/covid/cases/<region>', methods=['GET'])
def get_covid_cases_region(region):
    data = covid_data.get(region, covid_data['global'])
    return jsonify(data)


# Endpoint to update COVID-19 case count for a region
@app.route('/covid/cases/update', methods=['POST'])
def update_covid_cases():
    data = request.json
    region = data['region']
    new_cases = data['new_cases']
    if region in covid_data:
        covid_data[region]["cases"] += new_cases
    else:
        covid_data[region] = {"cases": new_cases, "deaths": 0, "recovered": 0}
    return jsonify({"message": f"Updated cases for {region}"})


# Endpoint to retrieve vaccination status
@app.route('/covid/vaccination-status', methods=['GET'])
def get_vaccination_status():
    return jsonify(vaccination_data)


# Endpoint to retrieve hospital resources
@app.route('/covid/hospitals/resources', methods=['GET'])
def get_hospital_resources():
    return jsonify(hospital_resources)


# Endpoint to update hospital resources
@app.route('/covid/hospitals/resources/update', methods=['POST'])
def update_hospital_resources():
    data = request.json
    hospital_resources.update(data)
    return jsonify({"message": "Hospital resources updated"})


if __name__ == '__main__':
    app.run(debug=True)
