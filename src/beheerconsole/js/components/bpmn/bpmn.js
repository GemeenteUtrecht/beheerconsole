import BpmnViewer from 'bpmn-js';

if (document.getElementById('bpmn-container')) {
    const viewer = new BpmnViewer({
        container: '#bpmn-container'
    });
    const xhr = new XMLHttpRequest();

    function handleResponse() {
        const xml = xhr.responseText;
        viewer.importXML(xml, function(err) {
            if (err) {
                console.log('error rendering', err);
            } else {
                console.log('rendered');
                var canvas = viewer.get('canvas');
                canvas.zoom('fit-viewport');
            }
        });
    }

    xhr.addEventListener("load", handleResponse);
    xhr.open("GET", "bpmn");
    xhr.send();
}
