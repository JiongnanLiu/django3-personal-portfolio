function loadChart(chart, url) {
    $.getJSON(url, (option => {
        chart.clear()
        chart.setOption(option)
    }))
}

function loadChart2(chart, url, callback) {
    $.getJSON(url, (data => {
        if (data['status'] === 'success') {
            chart.clear()
            chart.setOption(data['config'])
        } else {
            callback(data)
        }
    }))
}

function createChart(dom, width, height) {
    return LightweightCharts.createChart(dom, {
        width: width, height: height, localization: {dateFormat: "yyyy/MM/dd"}, priceScale: {mode: 1},
        watermark: {
            color: 'rgba(11, 94, 29, 0.4)',
            visible: true,
            text: 'ponentstock.com',
            fontSize: 24,
            horzAlign: 'left',
            vertAlign: 'top',
        }
    });
}

let chart_sereis = []
let legend_series = {}

function buildChart(chart, data) {
    chart_sereis.forEach(series => chart.removeSeries(series)) // 创建之前先清空

    buildCandlestick(chart, data) // 创建新的内容

    // 标题
    $('#legend-title').html(data['title'])

    // 添加事件响应
    chart.subscribeCrosshairMove((param) => {
        if (param.time) {
            Object.keys(legend_series).forEach((name) => {
                const price = param.seriesPrices.get(legend_series[name]['series'])
                const target = legend_series[name]['target']
                target.html('ma20:' + price)
            })
        } else {

        }
    })
}

function buildCandlestick(chart, data) {
    // k线图
    chart_sereis.push(buildCandlestickSeries(chart, data['quotes']))

    // 成交额
    const turnover = data['turnover']
    const turnoverSeries = chart.addHistogramSeries(turnover['config'])
    turnoverSeries.setData(turnover['data'])
    chart_sereis.push(turnoverSeries)

    // 所有线的创建
    const lines = data['lines']
    if (lines !== undefined) {
        Object.keys(lines).forEach(name => {
            const seriesData = lines[name]
            const lineSeries = chart.addLineSeries(seriesData['config'])
            lineSeries.setData(seriesData['data'])  // 赋值

            createPriceLine(lineSeries, seriesData['lines'] || []) // 画线
            lineSeries.setMarkers(seriesData['markers'] || []) // 标记

            // legend
            if (seriesData['legend'] !== false) {
                const color = seriesData['legend']['color']
                $('#legend-areas').append('<span id="legend_' + name + '" style="color:' + color + '"></span>')
                const target = $('#legend_' + name)
                target.html('ma20: 23.4')
                legend_series[name] = {'series': lineSeries, 'target': target}

                // 同时显示页面上的内容

            }


            chart_sereis.push(lineSeries)
        })
    }

    // 所有区域的创建
    const areas = data['areas']
    if (areas !== undefined) {
        Object.keys(areas).forEach(name => {
            const seriesData = areas[name]
            const areaSeries = chart.addAreaSeries(seriesData['config'])
            areaSeries.setData(seriesData['data'])  // 赋值

            chart_sereis.push(areaSeries)
        })
    }
}

function buildCandlestickSeries(chart, quotes) {
    const candlestickSeries = chart.addCandlestickSeries(quotes['config'] || {});  // 初始化对象
    candlestickSeries.setData(quotes['data']) // 赋值
    candlestickSeries.setMarkers(quotes['markers']) // 标记
    createPriceLine(candlestickSeries, quotes['lines'] || []) // 画线

    return candlestickSeries
}

function createPriceLine(series, lines) {
    lines.forEach(line => {
        series.createPriceLine(line)
    })
}

// ----------------------------------------------------------------------------------------------------------------
// datatable

datable_config = {
    "lengthMenu": [[25, 50, -1], [25, 50, "全部"]],
    "language": {
        "infoEmpty": "没有数据显示"
    },
    "searching": false,
    "scrollY": "540px",
    "scrollCollapse": true,
}

// 二次加载数据
function loadDataTable(target, config) {
    $(target).DataTable(Object.assign(datable_config, config || {}));
    $('.dataTables_length').addClass('bs-select');
}

// 搜索方法
function search(search_data, callback) {
    $.post('/screener/search/', search_data, (data => {
        if (data['success']) {
            $('#search_message').html(data['search_message'])
            $('#datatable_area').html(data['html'])

            loadDataTable($('#stock_datas'))  // 重新加载一次
        } else {
            // 显示错误信息
        }

        if (callback !== undefined)
            callback()
    }))
}

// 显示全局信息
function show_notice(message) {
    $('#top_message').html(message)
    $('#topMessageBox').modal('show')
}

$(function () {
    // 如果有全局性的消息通知，在这里显示
    // show_notice('新的版本已经上线了！')
})
