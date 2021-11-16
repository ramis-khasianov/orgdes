import React, { Component } from 'react';
import OrgChart from '@balkangraph/orgchart.js';
import classes from './MainChart.module.css'

class MainOrgchart extends Component {

    constructor(props) {
        super(props);
        this.divRef = React.createRef();
    }

    getNode(id) {
        return this.props.nodes.find(node => {return node.id === id})
    }

    shouldComponentUpdate() {
        return false;
    }

    componentDidMount() {
        OrgChart.templates.uc = Object.assign({}, OrgChart.templates.mery);
        OrgChart.templates.uc.plus = '<circle cx="15" cy="15" r="15" fill="#ffffff" stroke="#aeaeae" stroke-width="1"></circle>'
            + '<text text-anchor="middle" style="font-size: 14px;cursor:pointer;" fill="#757575" x="15" y="20">{collapsed-children-count}</text>';
        OrgChart.templates.uc.payroll = '<text style="font-size: 12px;" fill="#ffffff" x="8" y="65">ФОТ: {val}</text>';
        OrgChart.templates.uc.fte = '<text style="font-size: 14px;" fill="#ffffff" x="162" y="66">{val} FTE</text>';

        OrgChart.scroll.smooth = 10;
        OrgChart.scroll.speed = 10;

        this.chart = new OrgChart(this.divRef.current , {
            template: "uc",

            editForm: {
                buttons: {
                    share: null
                },
                generateElementsFromFields: false,
                elements: [
                    { type: 'textbox', label: 'ФИО', binding: 'fullName'},
                    { type: 'textbox', label: 'Должность', binding: 'jobTitle'},
                    { type: 'textbox', label: 'Департамент', binding: 'department'},
                    { type: 'textbox', label: 'Ставка', binding: 'employmentRate'},
                    { type: 'date', label: 'Дата приема', binding: 'hireDate'},
                    { type: 'date', label: 'Дата увольнения', binding: 'exitDate'},
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
                details: { text: "Профиль" },
                edit: { text: "Изменить" },
                add: { text: "Добавить подчиненного" }
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

        this.chart.on('init', (sender) => {
            sender.editUI.show(1);
        });

        this.chart.on('update', (sender, oldNode, newNode) => {
            let initialNode = this.getNode(newNode.id)

            for (let key in newNode) {
                if (newNode.hasOwnProperty(key)){
                    console.log(`${key}: ${initialNode[key]} -> ${newNode[key]}`)
                }
            }
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
