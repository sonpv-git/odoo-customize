/** @odoo-module **/

import { registry } from '@web/core/registry';
import { useService } from '@web/core/utils/hooks';
import { OwlChartRenderer } from './chart/chart_renderer';
import { RatingAmountChartRenderer } from './chart/chart_render_amount';
import { RatioKPIChartRenderer } from './chart/chart_render_ratio_kpi';
import { CriteriaPointsChartRenderer } from './chart/criteria_points_render';
import { KPIPlanChartRenderer } from './chart/chart_render_kpi_plan';
import { KPIAmountChartRenderer } from './chart/chart_render_kpi_amount';

const { Component, useState, onWillStart, onMounted } = owl;

export class OwlGreetDashboard extends Component {
  setup() {
    this.state = useState({
      title: 'Tổng hợp KPI theo phòng ban',
      kpiData: [],
      ratingAmountData: [],
      ratioKPIData: [],
      criteriaPointsData: [],
      kpiPlan: [],
      kpiAmount: [],
      departments: [],
      department_id: '',  // Giá trị mặc định là rỗng
      start_date: '',
      end_date: '',
    });

    this.orm = useService('orm');

    onWillStart(async () => {
      const data = await this.getKpiData();
      this.state.kpiData = data;
      this.state.ratingAmountData = data;
      this.state.ratioKPIData = data;
      this.state.criteriaPointsData = data;
      this.state.kpiPlan = data;
      this.state.kpiAmount = data;

      const departments = await this.getDepartments();
      this.state.departments = departments;
    });

    onMounted(() => {
      this.renderCharts();
    });
  }

  async getKpiData() {
    const params = new URLSearchParams({
      start_date: this.state.start_date,
      end_date: this.state.end_date,
    });

    // Chỉ thêm department_id vào params khi có giá trị
    if (this.state.department_id) {
      params.append('department_id', this.state.department_id);
    }

    console.log('Fetching data from:', `/check_method_get?${params.toString()}`);

    const response = await fetch(`/check_method_get?${params.toString()}`);
    const data = await response.json();
    return data;
  }

  async getDepartments() {
    const response = await fetch('/get_departments');
    const departments = await response.json();
    return departments;
  }

  async applyFilters() {
    console.log('Applying filters with department_id:', this.state.department_id);

    const data = await this.getKpiData();
    this.state.kpiData = data;
    this.state.ratingAmountData = data;
    this.state.ratioKPIData = data;
    this.state.criteriaPointsData = data;
    this.state.kpiPlan = data;
    this.state.kpiAmount = data;

    this.renderCharts();
  }

  renderCharts() {
    // Đảm bảo biểu đồ được render hoặc cập nhật đúng cách
    if (this.el) {
      this.el.querySelectorAll('.chart-container').forEach(chartContainer => {
        const chartComponent = chartContainer.__owl__.component;
        if (chartComponent && chartComponent.updateChart) {
          chartComponent.updateChart(this.state.kpiData);
        }
      });
    }
  }
}

OwlGreetDashboard.template = 'owl.OwlGreetDashboard';
OwlGreetDashboard.components = { OwlChartRenderer, RatingAmountChartRenderer, RatioKPIChartRenderer, CriteriaPointsChartRenderer, KPIPlanChartRenderer, KPIAmountChartRenderer };

registry.category('actions').add('owl.greet_dashboard', OwlGreetDashboard);
