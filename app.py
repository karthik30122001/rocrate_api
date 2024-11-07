from time import sleep
from flask import Flask, send_file, request, jsonify
from scripts.motus_ro_crates_preparer import MotusRoCratesPreparer

app = Flask(__name__)

@app.route('/process_crate', methods=['POST'])
def get_file():
    # Process data from request if necessary
    crate_url = request.get_json()["url"]
    # return file_path, 200
    # return send_file('lib/test.png', as_attachment=True), 200
    try:
        preparer = MotusRoCratesPreparer(crate_url, '.\scripts\out', extract_multiple=False)
        out_folder = preparer.prepare_motus_ro_crate()
        return send_file(out_folder+'.zip', as_attachment=True), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)