import flask
import pandas as pd


def create_app():
    app = flask.Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        """
        Index page view handler.
        :return: rendered index.html template
        """
        return flask.render_template('index.html')

    @app.route('/view', methods=['GET', 'POST'])
    def chart2():
        return flask.render_template('view.html')

    @app.route('/sd', methods=['GET', 'POST'])
    def sd():
        return flask.render_template('sd.html')

    @app.route('/data', methods=['GET', 'POST'])
    def data():
        """
        Data view handler
        :return: JSON object of the data CSV file
        """
        data = pd.read_csv('task_data.csv')

        class1 = data.loc[data['class_label'] == 1]
        class2 = data.loc[data['class_label'] == -1]

        

        context = {
            'class1': class1.to_dict(orient='list'),
            'class2': class2.to_dict(orient='list')
        }
        return flask.jsonify(context)

    return app


if __name__ == "__main__":
    app = create_app()
    # serve the application on port 7410
    app.run(host='0.0.0.0', port=7410)
