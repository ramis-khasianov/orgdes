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
            template: 'rony',
            nodes: this.props.nodes,

            nodeBinding: {
                field_0: "name",
                field_1: "title",
                img_0: "img"
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
