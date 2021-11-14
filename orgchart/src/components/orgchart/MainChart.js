import React, { Component } from 'react';
import OrgChart from '@balkangraph/orgchart.js';
import classes from './MainChart.module.css'

class MainOrgchart extends Component {

    constructor(props) {
        super(props);
        this.divRef = React.createRef();
    }

    shouldComponentUpdate() {
        return false;
    }

    componentDidMount() {
        this.chart = new OrgChart(this.divRef.current , {
            template: "olivia",

            editForm: {
                generateElementsFromFields: false,
                elements: [
                    { type: 'textbox', label: 'ФИО', binding: 'fullName'},
                    { type: 'textbox', label: 'Должность', binding: 'jobTitle'},
                    { type: 'textbox', label: 'Департамент', binding: 'department'},
                    { type: 'textbox', label: 'Ставка', binding: 'employmentRate'},
                    { type: 'date', label: 'Дата приема', binding: 'hireDate'},
                    { type: 'date', label: 'Дата увольнения', binding: 'exitDate'},
                    { type: 'date', label: 'Согласовано', binding: 'vacancyApprovedDate'},
                ]
            } ,

            enableSearch: true,
            enableDragDrop: true,
            menu: {
                pdf: { text: "Export PDF" },
                png: { text: "Export PNG" },
                svg: { text: "Export SVG" },
                csv: { text: "Export CSV" }
            },
            mouseScrool: OrgChart.action.scroll,
            layout: OrgChart.treeRightOffset,
            align: OrgChart.ORIENTATION,
            toolbar: {
                layout: true,
                zoom: true,
                fit: true,
                expandAll: true
            },
            nodeMenu: {
                details: { text: "Details" },
                edit: { text: "Edit" },
                add: { text: "Add" },
                remove: { text: "Remove" }
            },
            nodes: this.props.nodes,

            nodeBinding: {
                field_0: "name",
                field_1: "title",
                img_0: "img"
            }
        });

        this.chart.on('init', function(sender){
            sender.editUI.show(1);
        });
    }

    render() {
        return (
            <div className={classes.tree}>
                <div id="tree" ref={this.divRef}/>
            </div>
        );
    }
}

export default MainOrgchart
