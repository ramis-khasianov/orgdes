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
        OrgChart.templates.uc = Object.assign({}, OrgChart.templates.mery);
        OrgChart.templates.uc.payroll = '<text style="font-size: 12px;" fill="#ffffff" x="8" y="65">ФОТ: {val}</text>';
        OrgChart.templates.uc.fte = '<text style="font-size: 14px;" fill="#ffffff" x="162" y="66">{val} FTE</text>';

        this.chart = new OrgChart(this.divRef.current , {
            template: "uc",

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
                    { type: 'textbox', label: 'Оклад', binding: 'salary'},
                    { type: 'textbox', label: 'Условия бонуса', binding: 'bonusDescription'},
                    { type: 'textbox', label: 'ФОТ в месяц', binding: 'totalPayroll'},
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
                img_0: "img",
                fte: "allSubordinatesFte",
                payroll: "allSubordinatesPayrollText"
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
