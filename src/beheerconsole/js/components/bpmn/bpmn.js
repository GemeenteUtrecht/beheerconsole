import BpmnViewer from 'bpmn-js';

import request from '../../request';


const init = () => {
    const container = document.getElementById('bpmn-container');
    if (!container) {
        return;
    }

    const url = container.dataset.url;
    const viewer = new BpmnViewer({container: container});
    const canvas = viewer.get('canvas');

    request(url)
        .then(xml => {
            viewer.importXML(xml, (err) => {
                if (err) {
                    console.error(err);
                } else {
                    canvas.zoom('fit-viewport', 'auto');
                }
            });
        })
        .catch(console.error);
};

init();
