# Generated from 'https://sheets.googleapis.com//rest?version=v4'

# Until Python 4.0 we need this to allow forward type refs
from __future__ import annotations
from typing import Any, Dict, List, Literal, Optional, TypedDict, Union
import re
import requests
from login import login

scopes = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/spreadsheets.readonly',
]

def spreadsheets():
    token = login(scopes).token
    headers = {"Authorization": f"Bearer {token}"}
    return _spreadsheets(headers)


class _spreadsheets:

    def __init__(self, headers):
        self.headers = headers

    def batch_update(self, spreadsheet_id: str, request: BatchUpdateSpreadsheetRequest) -> BatchUpdateSpreadsheetResponse:
        """
        Applies one or more updates to the spreadsheet. Each request is validated before
        being applied. If any request is not valid then the entire request will fail and
        nothing will be applied. Some requests have replies to give you some information
        about how they are applied. The replies will mirror the requests. For example,
        if you applied 4 updates and the 3rd one had a reply, then the response will
        have 2 empty replies, the actual reply, and another empty reply, in that order.
        Due to the collaborative nature of spreadsheets, it is not guaranteed that the
        spreadsheet will reflect exactly your changes after this completes, however it
        is guaranteed that the updates in the request will be applied together
        atomically. Your changes may be altered with respect to collaborator changes. If
        there are no collaborators, the spreadsheet should reflect your changes.
        """
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}:batchUpdate"
        return requests.post(url, json=request, headers=self.headers).json()


    def create(self, request: Spreadsheet) -> Spreadsheet:
        "Creates a spreadsheet, returning the newly created spreadsheet."
        url = f"https://sheets.googleapis.com/v4/spreadsheets"
        return requests.post(url, json=request, headers=self.headers).json()


    def get(self, spreadsheet_id: str, include_grid_data: bool = False, ranges: List[str] = None) -> Spreadsheet:
        """
        Returns the spreadsheet at the given ID. The caller must specify the spreadsheet
        ID. By default, data within grids will not be returned. You can include grid
        data one of two ways: * Specify a field mask listing your desired fields using
        the `fields` URL parameter in HTTP * Set the includeGridData URL parameter to
        true. If a field mask is set, the `includeGridData` parameter is ignored For
        large spreadsheets, it is recommended to retrieve only the specific fields of
        the spreadsheet that you want. To retrieve only subsets of the spreadsheet, use
        the ranges URL parameter. Multiple ranges can be specified. Limiting the range
        will return only the portions of the spreadsheet that intersect the requested
        ranges. Ranges are specified using A1 notation.
        """
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}"
        params: Dict[str, Any] = {"includeGridData": include_grid_data, "ranges": ranges}
        return requests.get(url, params=params, headers=self.headers).json()


    def get_by_data_filter(self, spreadsheet_id: str, request: GetSpreadsheetByDataFilterRequest) -> Spreadsheet:
        """
        Returns the spreadsheet at the given ID. The caller must specify the spreadsheet
        ID. This method differs from GetSpreadsheet in that it allows selecting which
        subsets of spreadsheet data to return by specifying a dataFilters parameter.
        Multiple DataFilters can be specified. Specifying one or more data filters will
        return the portions of the spreadsheet that intersect ranges matched by any of
        the filters. By default, data within grids will not be returned. You can include
        grid data one of two ways: * Specify a field mask listing your desired fields
        using the `fields` URL parameter in HTTP * Set the includeGridData parameter to
        true. If a field mask is set, the `includeGridData` parameter is ignored For
        large spreadsheets, it is recommended to retrieve only the specific fields of
        the spreadsheet that you want.
        """
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}:getByDataFilter"
        return requests.post(url, json=request, headers=self.headers).json()


    def developerMetadata(self):
        return self._developerMetadata(self.headers)


    class _developerMetadata:

        def __init__(self, headers):
            self.headers = headers

        def get(self, spreadsheet_id: str, metadata_id: int) -> DeveloperMetadata:
            """
            Returns the developer metadata with the specified ID. The caller must specify
            the spreadsheet ID and the developer metadata's unique metadataId.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/developerMetadata/{metadata_id}"
            return requests.get(url, headers=self.headers).json()


        def search(self, spreadsheet_id: str, request: SearchDeveloperMetadataRequest) -> SearchDeveloperMetadataResponse:
            """
            Returns all developer metadata matching the specified DataFilter. If the
            provided DataFilter represents a DeveloperMetadataLookup object, this will
            return all DeveloperMetadata entries selected by it. If the DataFilter
            represents a location in a spreadsheet, this will return all developer metadata
            associated with locations intersecting that region.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/developerMetadata:search"
            return requests.post(url, json=request, headers=self.headers).json()


    def sheets(self):
        return self._sheets(self.headers)


    class _sheets:

        def __init__(self, headers):
            self.headers = headers

        def copy_to(self, spreadsheet_id: str, sheet_id: int, request: CopySheetToAnotherSpreadsheetRequest) -> SheetProperties:
            """
            Copies a single sheet from a spreadsheet to another spreadsheet. Returns the
            properties of the newly created sheet.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/sheets/{sheet_id}:copyTo"
            return requests.post(url, json=request, headers=self.headers).json()


    def values(self):
        return self._values(self.headers)


    class _values:

        def __init__(self, headers):
            self.headers = headers

        def append(self, spreadsheet_id: str, range: str, request: ValueRange, include_values_in_response: bool = False, insert_data_option: InsertDataOption = "OVERWRITE", response_date_time_render_option: DateTimeRenderOption = "SERIAL_NUMBER", response_value_render_option: ValueRenderOption = "FORMATTED_VALUE", value_input_option: InputValueOption = "INPUT_VALUE_OPTION_UNSPECIFIED") -> AppendValuesResponse:
            """
            Appends values to a spreadsheet. The input range is used to search for existing
            data and find a "table" within that range. Values will be appended to the next
            row of the table, starting with the first column of the table. See the
            [guide](/sheets/api/guides/values#appending_values) and [sample
            code](/sheets/api/samples/writing#append_values) for specific details of how
            tables are detected and data is appended. The caller must specify the
            spreadsheet ID, range, and a valueInputOption. The `valueInputOption` only
            controls how the input data will be added to the sheet (column-wise or row-
            wise), it does not influence what cell the data starts being written to.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range}:append"
            params: Dict[str, Any] = {"includeValuesInResponse": include_values_in_response, "insertDataOption": insert_data_option, "responseDateTimeRenderOption": response_date_time_render_option, "responseValueRenderOption": response_value_render_option, "valueInputOption": value_input_option}
            return requests.post(url, params=params, json=request, headers=self.headers).json()


        def batch_clear(self, spreadsheet_id: str, request: BatchClearValuesRequest) -> BatchClearValuesResponse:
            """
            Clears one or more ranges of values from a spreadsheet. The caller must specify
            the spreadsheet ID and one or more ranges. Only values are cleared -- all other
            properties of the cell (such as formatting, data validation, etc..) are kept.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values:batchClear"
            return requests.post(url, json=request, headers=self.headers).json()


        def batch_clear_by_data_filter(self, spreadsheet_id: str, request: BatchClearValuesByDataFilterRequest) -> BatchClearValuesByDataFilterResponse:
            """
            Clears one or more ranges of values from a spreadsheet. The caller must specify
            the spreadsheet ID and one or more DataFilters. Ranges matching any of the
            specified data filters will be cleared. Only values are cleared -- all other
            properties of the cell (such as formatting, data validation, etc..) are kept.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values:batchClearByDataFilter"
            return requests.post(url, json=request, headers=self.headers).json()


        def batch_get(self, spreadsheet_id: str, date_time_render_option: DateTimeRenderOption = "SERIAL_NUMBER", major_dimension: Dimension = "DIMENSION_UNSPECIFIED", ranges: List[str] = None, value_render_option: ValueRenderOption = "FORMATTED_VALUE") -> BatchGetValuesResponse:
            """
            Returns one or more ranges of values from a spreadsheet. The caller must specify
            the spreadsheet ID and one or more ranges.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values:batchGet"
            params: Dict[str, Any] = {"dateTimeRenderOption": date_time_render_option, "majorDimension": major_dimension, "ranges": ranges, "valueRenderOption": value_render_option}
            return requests.get(url, params=params, headers=self.headers).json()


        def batch_get_by_data_filter(self, spreadsheet_id: str, request: BatchGetValuesByDataFilterRequest) -> BatchGetValuesByDataFilterResponse:
            """
            Returns one or more ranges of values that match the specified data filters. The
            caller must specify the spreadsheet ID and one or more DataFilters. Ranges that
            match any of the data filters in the request will be returned.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values:batchGetByDataFilter"
            return requests.post(url, json=request, headers=self.headers).json()


        def batch_update(self, spreadsheet_id: str, request: BatchUpdateValuesRequest) -> BatchUpdateValuesResponse:
            """
            Sets values in one or more ranges of a spreadsheet. The caller must specify the
            spreadsheet ID, a valueInputOption, and one or more ValueRanges.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values:batchUpdate"
            return requests.post(url, json=request, headers=self.headers).json()


        def batch_update_by_data_filter(self, spreadsheet_id: str, request: BatchUpdateValuesByDataFilterRequest) -> BatchUpdateValuesByDataFilterResponse:
            """
            Sets values in one or more ranges of a spreadsheet. The caller must specify the
            spreadsheet ID, a valueInputOption, and one or more DataFilterValueRanges.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values:batchUpdateByDataFilter"
            return requests.post(url, json=request, headers=self.headers).json()


        def clear(self, spreadsheet_id: str, range: str, request: ClearValuesRequest) -> ClearValuesResponse:
            """
            Clears values from a spreadsheet. The caller must specify the spreadsheet ID and
            range. Only values are cleared -- all other properties of the cell (such as
            formatting, data validation, etc..) are kept.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range}:clear"
            return requests.post(url, json=request, headers=self.headers).json()


        def get(self, spreadsheet_id: str, range: str, date_time_render_option: DateTimeRenderOption = "SERIAL_NUMBER", major_dimension: Dimension = "DIMENSION_UNSPECIFIED", value_render_option: ValueRenderOption = "FORMATTED_VALUE") -> ValueRange:
            """
            Returns a range of values from a spreadsheet. The caller must specify the
            spreadsheet ID and a range.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range}"
            params: Dict[str, Any] = {"dateTimeRenderOption": date_time_render_option, "majorDimension": major_dimension, "valueRenderOption": value_render_option}
            return requests.get(url, params=params, headers=self.headers).json()


        def update(self, spreadsheet_id: str, range: str, request: ValueRange, include_values_in_response: bool = False, response_date_time_render_option: DateTimeRenderOption = "SERIAL_NUMBER", response_value_render_option: ValueRenderOption = "FORMATTED_VALUE", value_input_option: InputValueOption = "INPUT_VALUE_OPTION_UNSPECIFIED") -> UpdateValuesResponse:
            """
            Sets values in a range of a spreadsheet. The caller must specify the spreadsheet
            ID, range, and a valueInputOption.
            """
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range}"
            params: Dict[str, Any] = {"includeValuesInResponse": include_values_in_response, "responseDateTimeRenderOption": response_date_time_render_option, "responseValueRenderOption": response_value_render_option, "valueInputOption": value_input_option}
            return requests.put(url, params=params, headers=self.headers).json()


class AddBandingRequest(TypedDict):
    "Adds a new banded range to the spreadsheet."
    bandedRange: BandedRange

class AddBandingResponse(TypedDict):
    "The result of adding a banded range."
    bandedRange: BandedRange

class AddChartRequest(TypedDict):
    "Adds a chart to a sheet in the spreadsheet."
    chart: EmbeddedChart

class AddChartResponse(TypedDict):
    "The result of adding a chart to a spreadsheet."
    chart: EmbeddedChart

class AddConditionalFormatRuleRequest(TypedDict):
    """
    Adds a new conditional format rule at the given index. All subsequent rules'
    indexes are incremented.
    """
    index: int
    rule: ConditionalFormatRule

class AddDataSourceRequest(TypedDict):
    """
    Adds a data source. After the data source is added successfully, an associated
    DataSource sheet is created and an execution is triggered to refresh the sheet
    to read data from the data source. The request requires an additional
    bigquery.readonly OAuth scope.
    """
    dataSource: DataSource

class AddDataSourceResponse(TypedDict):
    "The result of adding a data source."
    dataExecutionStatus: DataExecutionStatus
    dataSource: DataSource

class AddDimensionGroupRequest(TypedDict):
    """
    Creates a group over the specified range. If the requested range is a superset
    of the range of an existing group G, then the depth of G is incremented and this
    new group G' has the depth of that group. For example, a group [C:D, depth 1] +
    [B:E] results in groups [B:E, depth 1] and [C:D, depth 2]. If the requested
    range is a subset of the range of an existing group G, then the depth of the new
    group G' becomes one greater than the depth of G. For example, a group [B:E,
    depth 1] + [C:D] results in groups [B:E, depth 1] and [C:D, depth 2]. If the
    requested range starts before and ends within, or starts within and ends after,
    the range of an existing group G, then the range of the existing group G becomes
    the union of the ranges, and the new group G' has depth one greater than the
    depth of G and range as the intersection of the ranges. For example, a group
    [B:D, depth 1] + [C:E] results in groups [B:E, depth 1] and [C:D, depth 2].
    """
    range: DimensionRange

class AddDimensionGroupResponse(TypedDict):
    "The result of adding a group."
    dimensionGroups: List[DimensionGroup]

class AddFilterViewRequest(TypedDict):
    "Adds a filter view."
    filter: FilterView

class AddFilterViewResponse(TypedDict):
    "The result of adding a filter view."
    filter: FilterView

class AddNamedRangeRequest(TypedDict):
    "Adds a named range to the spreadsheet."
    namedRange: NamedRange

class AddNamedRangeResponse(TypedDict):
    "The result of adding a named range."
    namedRange: NamedRange

class AddProtectedRangeRequest(TypedDict):
    "Adds a new protected range."
    protectedRange: ProtectedRange

class AddProtectedRangeResponse(TypedDict):
    "The result of adding a new protected range."
    protectedRange: ProtectedRange

class AddSheetRequest(TypedDict):
    """
    Adds a new sheet. When a sheet is added at a given index, all subsequent sheets'
    indexes are incremented. To add an object sheet, use AddChartRequest instead and
    specify EmbeddedObjectPosition.sheetId or EmbeddedObjectPosition.newSheet.
    """
    properties: SheetProperties

class AddSheetResponse(TypedDict):
    "The result of adding a sheet."
    properties: SheetProperties

class AddSlicerRequest(TypedDict):
    "Adds a slicer to a sheet in the spreadsheet."
    slicer: Slicer

class AddSlicerResponse(TypedDict):
    "The result of adding a slicer to a spreadsheet."
    slicer: Slicer

class AppendCellsRequest(TypedDict):
    """
    Adds new cells after the last row with data in a sheet, inserting new rows into
    the sheet if necessary.
    """
    fields: str
    rows: List[RowData]
    sheetId: int

class AppendDimensionRequest(TypedDict):
    "Appends rows or columns to the end of a sheet."
    dimension: Dimension
    length: int
    sheetId: int

class AppendValuesResponse(TypedDict):
    "The response when updating a range of values in a spreadsheet."
    spreadsheetId: str
    tableRange: str
    updates: UpdateValuesResponse

class AutoFillRequest(TypedDict):
    "Fills in more data based on existing data."
    range: GridRange
    sourceAndDestination: SourceAndDestination
    useAlternateSeries: bool

class AutoResizeDimensionsRequest(TypedDict):
    """
    Automatically resizes one or more dimensions based on the contents of the cells
    in that dimension.
    """
    dataSourceSheetDimensions: DataSourceSheetDimensionRange
    dimensions: DimensionRange

class BandedRange(TypedDict):
    "A banded (alternating colors) range in a sheet."
    bandedRangeId: Optional[int]
    columnProperties: BandingProperties
    range: GridRange
    rowProperties: BandingProperties

class BandingProperties(TypedDict):
    """
    Properties referring a single dimension (either row or column). If both
    BandedRange.row_properties and BandedRange.column_properties are set, the fill
    colors are applied to cells according to the following rules: * header_color and
    footer_color take priority over band colors. * first_band_color takes priority
    over second_band_color. * row_properties takes priority over column_properties.
    For example, the first row color takes priority over the first column color, but
    the first column color takes priority over the second row color. Similarly, the
    row header takes priority over the column header in the top left cell, but the
    column header takes priority over the first row color if the row header is not
    set.
    """
    firstBandColor: Color
    firstBandColorStyle: ColorStyle
    footerColor: Color
    footerColorStyle: ColorStyle
    headerColor: Color
    headerColorStyle: ColorStyle
    secondBandColor: Color
    secondBandColorStyle: ColorStyle

class BaselineValueFormat(TypedDict):
    "Formatting options for baseline value."
    comparisonType: ComparisonType
    description: str
    negativeColor: Color
    negativeColorStyle: ColorStyle
    position: TextPosition
    positiveColor: Color
    positiveColorStyle: ColorStyle
    textFormat: TextFormat

class BasicChartAxis(TypedDict):
    "An axis of the chart. A chart may not have more than one axis per axis position."
    format: TextFormat
    position: BasicChartAxisPosition
    title: str
    titleTextPosition: TextPosition
    viewWindowOptions: ChartAxisViewWindowOptions

class BasicChartDomain(TypedDict):
    """
    The domain of a chart. For example, if charting stock prices over time, this
    would be the date.
    """
    domain: ChartData
    reversed: bool

class BasicChartSeries(TypedDict):
    """
    A single series of data in a chart. For example, if charting stock prices over
    time, multiple series may exist, one for the "Open Price", "High Price", "Low
    Price" and "Close Price".
    """
    color: Color
    colorStyle: ColorStyle
    lineStyle: LineStyle
    series: ChartData
    targetAxis: BasicChartAxisPosition
    type: BasicChartType

class BasicChartSpec(TypedDict):
    """
    The specification for a basic chart. See BasicChartType for the list of charts
    this supports.
    """
    axis: List[BasicChartAxis]
    chartType: BasicChartType
    compareMode: BasicChartCompareMode
    domains: List[BasicChartDomain]
    headerCount: int
    interpolateNulls: bool
    legendPosition: BasicChartLegendPosition
    lineSmoothing: bool
    series: List[BasicChartSeries]
    stackedType: BasicChartStackedType
    threeDimensional: bool

class BasicFilter(TypedDict):
    "The default filter associated with a sheet."
    criteria: Dict[str, FilterCriteria]
    filterSpecs: List[FilterSpec]
    range: GridRange
    sortSpecs: List[SortSpec]

class BatchClearValuesByDataFilterRequest(TypedDict):
    """
    The request for clearing more than one range selected by a DataFilter in a
    spreadsheet.
    """
    dataFilters: List[DataFilter]

class BatchClearValuesByDataFilterResponse(TypedDict):
    """
    The response when clearing a range of values selected with DataFilters in a
    spreadsheet.
    """
    clearedRanges: List[str]
    spreadsheetId: str

class BatchClearValuesRequest(TypedDict):
    "The request for clearing more than one range of values in a spreadsheet."
    ranges: List[str]

class BatchClearValuesResponse(TypedDict):
    "The response when clearing a range of values in a spreadsheet."
    clearedRanges: List[str]
    spreadsheetId: str

class BatchGetValuesByDataFilterRequest(TypedDict):
    """
    The request for retrieving a range of values in a spreadsheet selected by a set
    of DataFilters.
    """
    dataFilters: List[DataFilter]
    dateTimeRenderOption: DateTimeRenderOption
    majorDimension: Dimension
    valueRenderOption: ValueRenderOption

class BatchGetValuesByDataFilterResponse(TypedDict):
    """
    The response when retrieving more than one range of values in a spreadsheet
    selected by DataFilters.
    """
    spreadsheetId: str
    valueRanges: List[MatchedValueRange]

class BatchGetValuesResponse(TypedDict):
    "The response when retrieving more than one range of values in a spreadsheet."
    spreadsheetId: str
    valueRanges: List[ValueRange]

class BatchUpdateSpreadsheetRequest(TypedDict):
    "The request for updating any aspect of a spreadsheet."
    includeSpreadsheetInResponse: bool
    requests: List[Request]
    responseIncludeGridData: bool
    responseRanges: List[str]

class BatchUpdateSpreadsheetResponse(TypedDict):
    "The reply for batch updating a spreadsheet."
    replies: List[Response]
    spreadsheetId: str
    updatedSpreadsheet: Spreadsheet

class BatchUpdateValuesByDataFilterRequest(TypedDict):
    "The request for updating more than one range of values in a spreadsheet."
    data: List[DataFilterValueRange]
    includeValuesInResponse: bool
    responseDateTimeRenderOption: DateTimeRenderOption
    responseValueRenderOption: ValueRenderOption
    valueInputOption: InputValueOption

class BatchUpdateValuesByDataFilterResponse(TypedDict):
    "The response when updating a range of values in a spreadsheet."
    responses: List[UpdateValuesByDataFilterResponse]
    spreadsheetId: str
    totalUpdatedCells: int
    totalUpdatedColumns: int
    totalUpdatedRows: int
    totalUpdatedSheets: int

class BatchUpdateValuesRequest(TypedDict):
    "The request for updating more than one range of values in a spreadsheet."
    data: List[ValueRange]
    includeValuesInResponse: bool
    responseDateTimeRenderOption: DateTimeRenderOption
    responseValueRenderOption: ValueRenderOption
    valueInputOption: InputValueOption

class BatchUpdateValuesResponse(TypedDict):
    "The response when updating a range of values in a spreadsheet."
    responses: List[UpdateValuesResponse]
    spreadsheetId: str
    totalUpdatedCells: int
    totalUpdatedColumns: int
    totalUpdatedRows: int
    totalUpdatedSheets: int

class BigQueryDataSourceSpec(TypedDict):
    "The specification of a BigQuery data source."
    projectId: str
    querySpec: BigQueryQuerySpec
    tableSpec: BigQueryTableSpec

class BigQueryQuerySpec(TypedDict):
    "Specifies a custom BigQuery query."
    rawQuery: str

class BigQueryTableSpec(TypedDict):
    "Specifies a BigQuery table definition. Only native tables is allowed."
    datasetId: str
    tableId: str
    tableProjectId: str

class BooleanCondition(TypedDict):
    """
    A condition that can evaluate to true or false. BooleanConditions are used by
    conditional formatting, data validation, and the criteria in filters.
    """
    type: ConditionType
    values: List[ConditionValue]

class BooleanRule(TypedDict):
    "A rule that may or may not match, depending on the condition."
    condition: BooleanCondition
    format: CellFormat

class Border(TypedDict):
    "A border along a cell."
    color: Color
    colorStyle: ColorStyle
    style: Style
    width: int

class Borders(TypedDict):
    "The borders of the cell."
    bottom: Border
    left: Border
    right: Border
    top: Border

class BubbleChartSpec(TypedDict):
    "A bubble chart."
    bubbleBorderColor: Color
    bubbleBorderColorStyle: ColorStyle
    bubbleLabels: ChartData
    bubbleMaxRadiusSize: int
    bubbleMinRadiusSize: int
    bubbleOpacity: float
    bubbleSizes: ChartData
    bubbleTextStyle: TextFormat
    domain: ChartData
    groupIds: ChartData
    legendPosition: BubbleChartLegendPosition
    series: ChartData

class CandlestickChartSpec(TypedDict):
    "A candlestick chart."
    data: List[CandlestickData]
    domain: CandlestickDomain

class CandlestickData(TypedDict):
    """
    The Candlestick chart data, each containing the low, open, close, and high
    values for a series.
    """
    closeSeries: CandlestickSeries
    highSeries: CandlestickSeries
    lowSeries: CandlestickSeries
    openSeries: CandlestickSeries

class CandlestickDomain(TypedDict):
    "The domain of a CandlestickChart."
    data: ChartData
    reversed: bool

class CandlestickSeries(TypedDict):
    "The series of a CandlestickData."
    data: ChartData

class CellData(TypedDict):
    "Data about a specific cell."
    dataSourceFormula: DataSourceFormula
    dataSourceTable: DataSourceTable
    dataValidation: DataValidationRule
    effectiveFormat: CellFormat
    effectiveValue: ExtendedValue
    formattedValue: str
    hyperlink: str
    note: str
    pivotTable: PivotTable
    textFormatRuns: List[TextFormatRun]
    userEnteredFormat: CellFormat
    userEnteredValue: ExtendedValue

class CellFormat(TypedDict):
    "The format of a cell."
    backgroundColor: Color
    backgroundColorStyle: ColorStyle
    borders: Borders
    horizontalAlignment: HorizontalAlign
    hyperlinkDisplayType: HyperlinkDisplayType
    numberFormat: NumberFormat
    padding: Padding
    textDirection: TextDirection
    textFormat: TextFormat
    textRotation: TextRotation
    verticalAlignment: VerticalAlign
    wrapStrategy: WrapStrategy

class ChartAxisViewWindowOptions(TypedDict):
    """
    The options that define a "view window" for a chart (such as the visible values
    in an axis).
    """
    viewWindowMax: float
    viewWindowMin: float
    viewWindowMode: ViewWindowMode

class ChartCustomNumberFormatOptions(TypedDict):
    "Custom number formatting options for chart attributes."
    prefix: str
    suffix: str

class ChartData(TypedDict):
    "The data included in a domain or series."
    aggregateType: ChartAggregateType
    columnReference: DataSourceColumnReference
    groupRule: ChartGroupRule
    sourceRange: ChartSourceRange

class ChartDateTimeRule(TypedDict):
    """
    Allows you to organize the date-time values in a source data column into buckets
    based on selected parts of their date or time values.
    """
    type: ChartDateTimeRuleType

class ChartGroupRule(TypedDict):
    """
    An optional setting on the ChartData of the domain of a data source chart that
    defines buckets for the values in the domain rather than breaking out each
    individual value. For example, when plotting a data source chart, you can
    specify a histogram rule on the domain (it should only contain numeric values),
    grouping its values into buckets. Any values of a chart series that fall into
    the same bucket are aggregated based on the aggregate_type.
    """
    dateTimeRule: ChartDateTimeRule
    histogramRule: ChartHistogramRule

class ChartHistogramRule(TypedDict):
    """
    Allows you to organize numeric values in a source data column into buckets of
    constant size.
    """
    intervalSize: float
    maxValue: float
    minValue: float

class ChartSourceRange(TypedDict):
    "Source ranges for a chart."
    sources: List[GridRange]

class ChartSpec(TypedDict):
    "The specifications of a chart."
    altText: str
    backgroundColor: Color
    backgroundColorStyle: ColorStyle
    basicChart: BasicChartSpec
    bubbleChart: BubbleChartSpec
    candlestickChart: CandlestickChartSpec
    dataSourceChartProperties: DataSourceChartProperties
    filterSpecs: List[FilterSpec]
    fontName: str
    hiddenDimensionStrategy: ChartHiddenDimensionStrategy
    histogramChart: HistogramChartSpec
    maximized: bool
    orgChart: OrgChartSpec
    pieChart: PieChartSpec
    scorecardChart: ScorecardChartSpec
    sortSpecs: List[SortSpec]
    subtitle: str
    subtitleTextFormat: TextFormat
    subtitleTextPosition: TextPosition
    title: str
    titleTextFormat: TextFormat
    titleTextPosition: TextPosition
    treemapChart: TreemapChartSpec
    waterfallChart: WaterfallChartSpec

class ClearBasicFilterRequest(TypedDict):
    "Clears the basic filter, if any exists on the sheet."
    sheetId: int

class ClearValuesRequest(TypedDict):
    "The request for clearing a range of values in a spreadsheet."

class ClearValuesResponse(TypedDict):
    "The response when clearing a range of values in a spreadsheet."
    clearedRange: str
    spreadsheetId: str

class Color(TypedDict):
    """
    Represents a color in the RGBA color space. This representation is designed for
    simplicity of conversion to/from color representations in various languages over
    compactness; for example, the fields of this representation can be trivially
    provided to the constructor of "java.awt.Color" in Java; it can also be
    trivially provided to UIColor's "+colorWithRed:green:blue:alpha" method in iOS;
    and, with just a little work, it can be easily formatted into a CSS "rgba()"
    string in JavaScript, as well. Note: this proto does not carry information about
    the absolute color space that should be used to interpret the RGB value (e.g.
    sRGB, Adobe RGB, DCI-P3, BT.2020, etc.). By default, applications SHOULD assume
    the sRGB color space. Note: when color equality needs to be decided,
    implementations, unless documented otherwise, will treat two colors to be equal
    if all their red, green, blue and alpha values each differ by at most 1e-5.
    Example (Java): import com.google.type.Color; // ... public static
    java.awt.Color fromProto(Color protocolor) { float alpha = protocolor.hasAlpha()
    ? protocolor.getAlpha().getValue() : 1.0; return new java.awt.Color(
    protocolor.getRed(), protocolor.getGreen(), protocolor.getBlue(), alpha); }
    public static Color toProto(java.awt.Color color) { float red = (float)
    color.getRed(); float green = (float) color.getGreen(); float blue = (float)
    color.getBlue(); float denominator = 255.0; Color.Builder resultBuilder = Color
    .newBuilder() .setRed(red / denominator) .setGreen(green / denominator)
    .setBlue(blue / denominator); int alpha = color.getAlpha(); if (alpha != 255) {
    result.setAlpha( FloatValue .newBuilder() .setValue(((float) alpha) /
    denominator) .build()); } return resultBuilder.build(); } // ... Example (iOS /
    Obj-C): // ... static UIColor* fromProto(Color* protocolor) { float red =
    [protocolor red]; float green = [protocolor green]; float blue = [protocolor
    blue]; FloatValue* alpha_wrapper = [protocolor alpha]; float alpha = 1.0; if
    (alpha_wrapper != nil) { alpha = [alpha_wrapper value]; } return [UIColor
    colorWithRed:red green:green blue:blue alpha:alpha]; } static Color*
    toProto(UIColor* color) { CGFloat red, green, blue, alpha; if (![color
    getRed:&red green:&green blue:&blue alpha:&alpha]) { return nil; } Color* result
    = [[Color alloc] init]; [result setRed:red]; [result setGreen:green]; [result
    setBlue:blue]; if (alpha <= 0.9999) { [result
    setAlpha:floatWrapperWithValue(alpha)]; } [result autorelease]; return result; }
    // ... Example (JavaScript): // ... var protoToCssColor = function(rgb_color) {
    var redFrac = rgb_color.red || 0.0; var greenFrac = rgb_color.green || 0.0; var
    blueFrac = rgb_color.blue || 0.0; var red = Math.floor(redFrac * 255); var green
    = Math.floor(greenFrac * 255); var blue = Math.floor(blueFrac * 255); if
    (!('alpha' in rgb_color)) { return rgbToCssColor_(red, green, blue); } var
    alphaFrac = rgb_color.alpha.value || 0.0; var rgbParams = [red, green,
    blue].join(','); return ['rgba(', rgbParams, ',', alphaFrac, ')'].join(''); };
    var rgbToCssColor_ = function(red, green, blue) { var rgbNumber = new
    Number((red << 16) | (green << 8) | blue); var hexString =
    rgbNumber.toString(16); var missingZeros = 6 - hexString.length; var
    resultBuilder = ['#']; for (var i = 0; i < missingZeros; i++) {
    resultBuilder.push('0'); } resultBuilder.push(hexString); return
    resultBuilder.join(''); }; // ...
    """
    alpha: float
    blue: float
    green: float
    red: float

class ColorStyle(TypedDict):
    "A color value."
    rgbColor: Color
    themeColor: ThemeColorType

class ConditionValue(TypedDict):
    "The value of the condition."
    relativeDate: RelativeDate
    userEnteredValue: str

class ConditionalFormatRule(TypedDict):
    "A rule describing a conditional format."
    booleanRule: BooleanRule
    gradientRule: GradientRule
    ranges: List[GridRange]

class CopyPasteRequest(TypedDict):
    "Copies data from the source to the destination."
    destination: GridRange
    pasteOrientation: PasteOrientation
    pasteType: PasteType
    source: GridRange

class CopySheetToAnotherSpreadsheetRequest(TypedDict):
    "The request to copy a sheet across spreadsheets."
    destinationSpreadsheetId: str

class CreateDeveloperMetadataRequest(TypedDict):
    "A request to create developer metadata."
    developerMetadata: DeveloperMetadata

class CreateDeveloperMetadataResponse(TypedDict):
    "The response from creating developer metadata."
    developerMetadata: DeveloperMetadata

class CutPasteRequest(TypedDict):
    "Moves data from the source to the destination."
    destination: GridCoordinate
    pasteType: PasteType
    source: GridRange

class DataExecutionStatus(TypedDict):
    "The data execution status."
    errorCode: DataExecutionErrorCode
    errorMessage: str
    lastRefreshTime: str
    state: DataExecutionState

class DataFilter(TypedDict):
    "Filter that describes what data should be selected or returned from a request."
    a1Range: str
    developerMetadataLookup: DeveloperMetadataLookup
    gridRange: GridRange

class DataFilterValueRange(TypedDict):
    "A range of values whose location is specified by a DataFilter."
    dataFilter: DataFilter
    majorDimension: Dimension
    values: List[List[Any]]

class DataSource(TypedDict):
    "Information about an external data source in the spreadsheet."
    calculatedColumns: List[DataSourceColumn]
    dataSourceId: str
    sheetId: int
    spec: DataSourceSpec

class DataSourceChartProperties(TypedDict):
    "Properties of a data source chart."
    dataExecutionStatus: DataExecutionStatus
    dataSourceId: str

class DataSourceColumn(TypedDict):
    "A data source column."
    formula: str
    reference: DataSourceColumnReference

class DataSourceColumnReference(TypedDict):
    "An unique identifier that references to a data source column."
    name: str

class DataSourceFormula(TypedDict):
    "A data source formula."
    dataExecutionStatus: DataExecutionStatus
    dataSourceId: str

class DataSourceObjectReference(TypedDict):
    "Reference to a data source object."
    chartId: int
    dataSourceFormulaCell: GridCoordinate
    dataSourcePivotTableAnchorCell: GridCoordinate
    dataSourceTableAnchorCell: GridCoordinate
    sheetId: str

class DataSourceObjectReferences(TypedDict):
    "A list of references to data source objects."
    references: List[DataSourceObjectReference]

class DataSourceParameter(TypedDict):
    """
    A parameter in a data source's query. The parameter allows user to pass in
    values from the spreadsheet into a query.
    """
    name: str
    namedRangeId: str
    range: GridRange

class DataSourceRefreshDailySchedule(TypedDict):
    "Schedule refreshes in a time interval everyday."
    startTime: TimeOfDay

class DataSourceRefreshMonthlySchedule(TypedDict):
    """
    Schedule refreshes in a time interval on specified days in a month and repeats
    monthly.
    """
    daysOfMonth: List[int]
    startTime: TimeOfDay

class DataSourceRefreshSchedule(TypedDict):
    """
    The data source refresh schedule. All data sources in the spreadsheet are
    scheduled to refresh in a future time interval. The time interval size defaults
    to the one defined in the Sheets editor. For example, if a daily schedule at
    start time of 8am is scheduled, and the time interval is 4 hours, the scheduled
    refresh will happen between 8am and 12pm every day.
    """
    dailySchedule: DataSourceRefreshDailySchedule
    enabled: bool
    monthlySchedule: DataSourceRefreshMonthlySchedule
    nextRun: Interval
    refreshScope: DataSourceRefreshScope
    weeklySchedule: DataSourceRefreshWeeklySchedule

class DataSourceRefreshWeeklySchedule(TypedDict):
    """
    Schedule refreshes in a time interval on specified days in a week and repeats
    weekly.
    """
    daysOfWeek: List[DayOfWeek]
    startTime: TimeOfDay

class DataSourceSheetDimensionRange(TypedDict):
    "A range along a single dimension on a DataSource sheet."
    columnReferences: List[DataSourceColumnReference]
    sheetId: int

class DataSourceSheetProperties(TypedDict):
    "Additional properties of a SheetType.DATA_SOURCE sheet."
    columns: List[DataSourceColumn]
    dataExecutionStatus: DataExecutionStatus
    dataSourceId: str

class DataSourceSpec(TypedDict):
    "The specification of a data source."
    bigQuery: BigQueryDataSourceSpec
    parameters: List[DataSourceParameter]

class DataSourceTable(TypedDict):
    """
    A data source table, allowing to import a static table of data from the
    DataSource into Sheets. This is also known as "Extract" in the Sheets editor.
    """
    columnSelectionType: DataSourceTableColumnSelectionType
    columns: List[DataSourceColumnReference]
    dataExecutionStatus: DataExecutionStatus
    dataSourceId: str
    filterSpecs: List[FilterSpec]
    rowLimit: int
    sortSpecs: List[SortSpec]

class DataValidationRule(TypedDict):
    "A data validation rule."
    condition: BooleanCondition
    inputMessage: str
    showCustomUi: bool
    strict: bool

class DateTimeRule(TypedDict):
    """
    Allows you to organize the date-time values in a source data column into buckets
    based on selected parts of their date or time values. For example, consider a
    pivot table showing sales transactions by date: +----------+--------------+ |
    Date | SUM of Sales | +----------+--------------+ | 1/1/2017 | $621.14 | |
    2/3/2017 | $708.84 | | 5/8/2017 | $326.84 | ... +----------+--------------+
    Applying a date-time group rule with a DateTimeRuleType of YEAR_MONTH results in
    the following pivot table. +--------------+--------------+ | Grouped Date | SUM
    of Sales | +--------------+--------------+ | 2017-Jan | $53,731.78 | | 2017-Feb
    | $83,475.32 | | 2017-Mar | $94,385.05 | ... +--------------+--------------+
    """
    type: DateTimeRuleType

class DeleteBandingRequest(TypedDict):
    "Removes the banded range with the given ID from the spreadsheet."
    bandedRangeId: int

class DeleteConditionalFormatRuleRequest(TypedDict):
    """
    Deletes a conditional format rule at the given index. All subsequent rules'
    indexes are decremented.
    """
    index: int
    sheetId: int

class DeleteConditionalFormatRuleResponse(TypedDict):
    "The result of deleting a conditional format rule."
    rule: ConditionalFormatRule

class DeleteDataSourceRequest(TypedDict):
    """
    Deletes a data source. The request also deletes the associated data source
    sheet, and unlinks all associated data source objects.
    """
    dataSourceId: str

class DeleteDeveloperMetadataRequest(TypedDict):
    "A request to delete developer metadata."
    dataFilter: DataFilter

class DeleteDeveloperMetadataResponse(TypedDict):
    "The response from deleting developer metadata."
    deletedDeveloperMetadata: List[DeveloperMetadata]

class DeleteDimensionGroupRequest(TypedDict):
    """
    Deletes a group over the specified range by decrementing the depth of the
    dimensions in the range. For example, assume the sheet has a depth-1 group over
    B:E and a depth-2 group over C:D. Deleting a group over D:E leaves the sheet
    with a depth-1 group over B:D and a depth-2 group over C:C.
    """
    range: DimensionRange

class DeleteDimensionGroupResponse(TypedDict):
    "The result of deleting a group."
    dimensionGroups: List[DimensionGroup]

class DeleteDimensionRequest(TypedDict):
    "Deletes the dimensions from the sheet."
    range: DimensionRange

class DeleteDuplicatesRequest(TypedDict):
    """
    Removes rows within this range that contain values in the specified columns that
    are duplicates of values in any previous row. Rows with identical values but
    different letter cases, formatting, or formulas are considered to be duplicates.
    This request also removes duplicate rows hidden from view (for example, due to a
    filter). When removing duplicates, the first instance of each duplicate row
    scanning from the top downwards is kept in the resulting range. Content outside
    of the specified range isn't removed, and rows considered duplicates do not have
    to be adjacent to each other in the range.
    """
    comparisonColumns: List[DimensionRange]
    range: GridRange

class DeleteDuplicatesResponse(TypedDict):
    "The result of removing duplicates in a range."
    duplicatesRemovedCount: int

class DeleteEmbeddedObjectRequest(TypedDict):
    "Deletes the embedded object with the given ID."
    objectId: int

class DeleteFilterViewRequest(TypedDict):
    "Deletes a particular filter view."
    filterId: int

class DeleteNamedRangeRequest(TypedDict):
    "Removes the named range with the given ID from the spreadsheet."
    namedRangeId: str

class DeleteProtectedRangeRequest(TypedDict):
    "Deletes the protected range with the given ID."
    protectedRangeId: int

class DeleteRangeRequest(TypedDict):
    "Deletes a range of cells, shifting other cells into the deleted area."
    range: GridRange
    shiftDimension: Dimension

class DeleteSheetRequest(TypedDict):
    "Deletes the requested sheet."
    sheetId: int

class DeveloperMetadata(TypedDict):
    """
    Developer metadata associated with a location or object in a spreadsheet.
    Developer metadata may be used to associate arbitrary data with various parts of
    a spreadsheet and will remain associated at those locations as they move around
    and the spreadsheet is edited. For example, if developer metadata is associated
    with row 5 and another row is then subsequently inserted above row 5, that
    original metadata will still be associated with the row it was first associated
    with (what is now row 6). If the associated object is deleted its metadata is
    deleted too.
    """
    location: DeveloperMetadataLocation
    metadataId: int
    metadataKey: str
    metadataValue: str
    visibility: DeveloperMetadataVisibility

class DeveloperMetadataLocation(TypedDict):
    "A location where metadata may be associated in a spreadsheet."
    dimensionRange: DimensionRange
    locationType: DeveloperMetadataLocationType
    sheetId: int
    spreadsheet: bool

class DeveloperMetadataLookup(TypedDict):
    """
    Selects DeveloperMetadata that matches all of the specified fields. For example,
    if only a metadata ID is specified this considers the DeveloperMetadata with
    that particular unique ID. If a metadata key is specified, this considers all
    developer metadata with that key. If a key, visibility, and location type are
    all specified, this considers all developer metadata with that key and
    visibility that are associated with a location of that type. In general, this
    selects all DeveloperMetadata that matches the intersection of all the specified
    fields; any field or combination of fields may be specified.
    """
    locationMatchingStrategy: DeveloperMetadataLocationMatchingStrategy
    locationType: DeveloperMetadataLocationType
    metadataId: int
    metadataKey: str
    metadataLocation: DeveloperMetadataLocation
    metadataValue: str
    visibility: DeveloperMetadataVisibility

class DimensionGroup(TypedDict):
    """
    A group over an interval of rows or columns on a sheet, which can contain or be
    contained within other groups. A group can be collapsed or expanded as a unit on
    the sheet.
    """
    collapsed: bool
    depth: int
    range: DimensionRange

class DimensionProperties(TypedDict):
    "Properties about a dimension."
    dataSourceColumnReference: DataSourceColumnReference
    developerMetadata: List[DeveloperMetadata]
    hiddenByFilter: bool
    hiddenByUser: bool
    pixelSize: int

class DimensionRange(TypedDict):
    """
    A range along a single dimension on a sheet. All indexes are zero-based. Indexes
    are half open: the start index is inclusive and the end index is exclusive.
    Missing indexes indicate the range is unbounded on that side.
    """
    dimension: Dimension
    endIndex: int
    sheetId: int
    startIndex: int

class DuplicateFilterViewRequest(TypedDict):
    "Duplicates a particular filter view."
    filterId: int

class DuplicateFilterViewResponse(TypedDict):
    "The result of a filter view being duplicated."
    filter: FilterView

class DuplicateSheetRequest(TypedDict):
    "Duplicates the contents of a sheet."
    insertSheetIndex: int
    newSheetId: int
    newSheetName: str
    sourceSheetId: int

class DuplicateSheetResponse(TypedDict):
    "The result of duplicating a sheet."
    properties: SheetProperties

class Editors(TypedDict):
    "The editors of a protected range."
    domainUsersCanEdit: bool
    groups: List[str]
    users: List[str]

class EmbeddedChart(TypedDict):
    "A chart embedded in a sheet."
    chartId: int
    position: EmbeddedObjectPosition
    spec: ChartSpec

class EmbeddedObjectPosition(TypedDict):
    "The position of an embedded object such as a chart."
    newSheet: bool
    overlayPosition: OverlayPosition
    sheetId: int

class ErrorValue(TypedDict):
    "An error in a cell."
    message: str
    type: ErrorType

class ExtendedValue(TypedDict):
    "The kinds of value that a cell in a spreadsheet can have."
    boolValue: bool
    errorValue: ErrorValue
    formulaValue: str
    numberValue: float
    stringValue: str

class FilterCriteria(TypedDict):
    "Criteria for showing/hiding rows in a filter or filter view."
    condition: BooleanCondition
    hiddenValues: List[str]
    visibleBackgroundColor: Color
    visibleBackgroundColorStyle: ColorStyle
    visibleForegroundColor: Color
    visibleForegroundColorStyle: ColorStyle

class FilterSpec(TypedDict):
    "The filter criteria associated with a specific column."
    columnIndex: int
    dataSourceColumnReference: DataSourceColumnReference
    filterCriteria: FilterCriteria

class FilterView(TypedDict):
    "A filter view."
    criteria: Dict[str, FilterCriteria]
    filterSpecs: List[FilterSpec]
    filterViewId: int
    namedRangeId: str
    range: GridRange
    sortSpecs: List[SortSpec]
    title: str

class FindReplaceRequest(TypedDict):
    "Finds and replaces data in cells over a range, sheet, or all sheets."
    allSheets: bool
    find: str
    includeFormulas: bool
    matchCase: bool
    matchEntireCell: bool
    range: GridRange
    replacement: str
    searchByRegex: bool
    sheetId: int

class FindReplaceResponse(TypedDict):
    "The result of the find/replace."
    formulasChanged: int
    occurrencesChanged: int
    rowsChanged: int
    sheetsChanged: int
    valuesChanged: int

class GetSpreadsheetByDataFilterRequest(TypedDict):
    "The request for retrieving a Spreadsheet."
    dataFilters: List[DataFilter]
    includeGridData: bool

class GradientRule(TypedDict):
    """
    A rule that applies a gradient color scale format, based on the interpolation
    points listed. The format of a cell will vary based on its contents as compared
    to the values of the interpolation points.
    """
    maxpoint: InterpolationPoint
    midpoint: InterpolationPoint
    minpoint: InterpolationPoint

class GridCoordinate(TypedDict):
    "A coordinate in a sheet. All indexes are zero-based."
    columnIndex: int
    rowIndex: int
    sheetId: int

class GridData(TypedDict):
    "Data in the grid, as well as metadata about the dimensions."
    columnMetadata: List[DimensionProperties]
    rowData: List[RowData]
    rowMetadata: List[DimensionProperties]
    startColumn: int
    startRow: int

class GridProperties(TypedDict):
    "Properties of a grid."
    columnCount: int
    columnGroupControlAfter: bool
    frozenColumnCount: int
    frozenRowCount: int
    hideGridlines: bool
    rowCount: int
    rowGroupControlAfter: bool

class GridRange(TypedDict):
    """
    A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the
    start index is inclusive and the end index is exclusive -- [start_index,
    end_index). Missing indexes indicate the range is unbounded on that side. For
    example, if `"Sheet1"` is sheet ID 0, then: `Sheet1!A1:A1 == sheet_id: 0,
    start_row_index: 0, end_row_index: 1, start_column_index: 0, end_column_index:
    1` `Sheet1!A3:B4 == sheet_id: 0, start_row_index: 2, end_row_index: 4,
    start_column_index: 0, end_column_index: 2` `Sheet1!A:B == sheet_id: 0,
    start_column_index: 0, end_column_index: 2` `Sheet1!A5:B == sheet_id: 0,
    start_row_index: 4, start_column_index: 0, end_column_index: 2` `Sheet1 ==
    sheet_id:0` The start index must always be less than or equal to the end index.
    If the start index equals the end index, then the range is empty. Empty ranges
    are typically not meaningful and are usually rendered in the UI as `#REF!`.
    """
    endColumnIndex: int
    endRowIndex: int
    sheetId: int
    startColumnIndex: int
    startRowIndex: int

class HistogramChartSpec(TypedDict):
    """
    A histogram chart. A histogram chart groups data items into bins, displaying
    each bin as a column of stacked items. Histograms are used to display the
    distribution of a dataset. Each column of items represents a range into which
    those items fall. The number of bins can be chosen automatically or specified
    explicitly.
    """
    bucketSize: float
    legendPosition: HistogramChartLegendPosition
    outlierPercentile: float
    series: List[HistogramSeries]
    showItemDividers: bool

class HistogramRule(TypedDict):
    """
    Allows you to organize the numeric values in a source data column into buckets
    of a constant size. All values from HistogramRule.start to HistogramRule.end are
    placed into groups of size HistogramRule.interval. In addition, all values below
    HistogramRule.start are placed in one group, and all values above
    HistogramRule.end are placed in another. Only HistogramRule.interval is
    required, though if HistogramRule.start and HistogramRule.end are both provided,
    HistogramRule.start must be less than HistogramRule.end. For example, a pivot
    table showing average purchase amount by age that has 50+ rows:
    +-----+-------------------+ | Age | AVERAGE of Amount |
    +-----+-------------------+ | 16 | $27.13 | | 17 | $5.24 | | 18 | $20.15 | ...
    +-----+-------------------+ could be turned into a pivot table that looks like
    the one below by applying a histogram group rule with a HistogramRule.start of
    25, an HistogramRule.interval of 20, and an HistogramRule.end of 65.
    +-------------+-------------------+ | Grouped Age | AVERAGE of Amount |
    +-------------+-------------------+ | < 25 | $19.34 | | 25-45 | $31.43 | | 45-65
    | $35.87 | | > 65 | $27.55 | +-------------+-------------------+ | Grand Total |
    $29.12 | +-------------+-------------------+
    """
    end: float
    interval: float
    start: float

class HistogramSeries(TypedDict):
    "A histogram series containing the series color and data."
    barColor: Color
    barColorStyle: ColorStyle
    data: ChartData

class InsertDimensionRequest(TypedDict):
    "Inserts rows or columns in a sheet at a particular index."
    inheritFromBefore: bool
    range: DimensionRange

class InsertRangeRequest(TypedDict):
    "Inserts cells into a range, shifting the existing cells over or down."
    range: GridRange
    shiftDimension: Dimension

class InterpolationPoint(TypedDict):
    """
    A single interpolation point on a gradient conditional format. These pin the
    gradient color scale according to the color, type and value chosen.
    """
    color: Color
    colorStyle: ColorStyle
    type: InterpolationPointType
    value: str

class Interval(TypedDict):
    """
    Represents a time interval, encoded as a Timestamp start (inclusive) and a
    Timestamp end (exclusive). The start must be less than or equal to the end. When
    the start equals the end, the interval is empty (matches no time). When both
    start and end are unspecified, the interval matches any time.
    """
    endTime: str
    startTime: str

class IterativeCalculationSettings(TypedDict):
    """
    Settings to control how circular dependencies are resolved with iterative
    calculation.
    """
    convergenceThreshold: float
    maxIterations: int

class KeyValueFormat(TypedDict):
    "Formatting options for key value."
    position: TextPosition
    textFormat: TextFormat

class LineStyle(TypedDict):
    "Properties that describe the style of a line."
    type: LineDashType
    width: int

class ManualRule(TypedDict):
    """
    Allows you to manually organize the values in a source data column into buckets
    with names of your choosing. For example, a pivot table that aggregates
    population by state: +-------+-------------------+ | State | SUM of Population |
    +-------+-------------------+ | AK | 0.7 | | AL | 4.8 | | AR | 2.9 | ...
    +-------+-------------------+ could be turned into a pivot table that aggregates
    population by time zone by providing a list of groups (for example, groupName =
    'Central', items = ['AL', 'AR', 'IA', ...]) to a manual group rule. Note that a
    similar effect could be achieved by adding a time zone column to the source data
    and adjusting the pivot table. +-----------+-------------------+ | Time Zone |
    SUM of Population | +-----------+-------------------+ | Central | 106.3 | |
    Eastern | 151.9 | | Mountain | 17.4 | ... +-----------+-------------------+
    """
    groups: List[ManualRuleGroup]

class ManualRuleGroup(TypedDict):
    """
    A group name and a list of items from the source data that should be placed in
    the group with this name.
    """
    groupName: ExtendedValue
    items: List[ExtendedValue]

class MatchedDeveloperMetadata(TypedDict):
    """
    A developer metadata entry and the data filters specified in the original
    request that matched it.
    """
    dataFilters: List[DataFilter]
    developerMetadata: DeveloperMetadata

class MatchedValueRange(TypedDict):
    "A value range that was matched by one or more data filers."
    dataFilters: List[DataFilter]
    valueRange: ValueRange

class MergeCellsRequest(TypedDict):
    "Merges all cells in the range."
    mergeType: MergeType
    range: GridRange

class MoveDimensionRequest(TypedDict):
    "Moves one or more rows or columns."
    destinationIndex: int
    source: DimensionRange

class NamedRange(TypedDict):
    "A named range."
    name: str
    namedRangeId: str
    range: GridRange

class NumberFormat(TypedDict):
    "The number format of a cell."
    pattern: str
    type: NumberFormatType

class OrgChartSpec(TypedDict):
    """
    An org chart. Org charts require a unique set of labels in labels and may
    optionally include parent_labels and tooltips. parent_labels contain, for each
    node, the label identifying the parent node. tooltips contain, for each node, an
    optional tooltip. For example, to describe an OrgChart with Alice as the CEO,
    Bob as the President (reporting to Alice) and Cathy as VP of Sales (also
    reporting to Alice), have labels contain "Alice", "Bob", "Cathy", parent_labels
    contain "", "Alice", "Alice" and tooltips contain "CEO", "President", "VP
    Sales".
    """
    labels: ChartData
    nodeColor: Color
    nodeColorStyle: ColorStyle
    nodeSize: OrgChartLabelSize
    parentLabels: ChartData
    selectedNodeColor: Color
    selectedNodeColorStyle: ColorStyle
    tooltips: ChartData

class OverlayPosition(TypedDict):
    "The location an object is overlaid on top of a grid."
    anchorCell: GridCoordinate
    heightPixels: int
    offsetXPixels: int
    offsetYPixels: int
    widthPixels: int

class Padding(TypedDict):
    """
    The amount of padding around the cell, in pixels. When updating padding, every
    field must be specified.
    """
    bottom: int
    left: int
    right: int
    top: int

class PasteDataRequest(TypedDict):
    "Inserts data into the spreadsheet starting at the specified coordinate."
    coordinate: GridCoordinate
    data: str
    delimiter: str
    html: bool
    type: PasteType

class PieChartSpec(TypedDict):
    "A pie chart."
    domain: ChartData
    legendPosition: PieChartLegendPosition
    pieHole: float
    series: ChartData
    threeDimensional: bool

class PivotFilterCriteria(TypedDict):
    "Criteria for showing/hiding rows in a pivot table."
    visibleValues: List[str]

class PivotFilterSpec(TypedDict):
    "The pivot table filter criteria associated with a specific source column offset."
    columnOffsetIndex: int
    dataSourceColumnReference: DataSourceColumnReference
    filterCriteria: PivotFilterCriteria

class PivotGroup(TypedDict):
    "A single grouping (either row or column) in a pivot table."
    dataSourceColumnReference: DataSourceColumnReference
    groupLimit: PivotGroupLimit
    groupRule: PivotGroupRule
    label: str
    repeatHeadings: bool
    showTotals: bool
    sortOrder: SortOrder
    sourceColumnOffset: int
    valueBucket: PivotGroupSortValueBucket
    valueMetadata: List[PivotGroupValueMetadata]

class PivotGroupLimit(TypedDict):
    "The count limit on rows or columns in the pivot group."
    applyOrder: int
    countLimit: int

class PivotGroupRule(TypedDict):
    """
    An optional setting on a PivotGroup that defines buckets for the values in the
    source data column rather than breaking out each individual value. Only one
    PivotGroup with a group rule may be added for each column in the source data,
    though on any given column you may add both a PivotGroup that has a rule and a
    PivotGroup that does not.
    """
    dateTimeRule: DateTimeRule
    histogramRule: HistogramRule
    manualRule: ManualRule

class PivotGroupSortValueBucket(TypedDict):
    "Information about which values in a pivot group should be used for sorting."
    buckets: List[ExtendedValue]
    valuesIndex: int

class PivotGroupValueMetadata(TypedDict):
    "Metadata about a value in a pivot grouping."
    collapsed: bool
    value: ExtendedValue

class PivotTable(TypedDict):
    "A pivot table."
    columns: List[PivotGroup]
    criteria: Dict[str, PivotFilterCriteria]
    dataExecutionStatus: DataExecutionStatus
    dataSourceId: str
    filterSpecs: List[PivotFilterSpec]
    rows: List[PivotGroup]
    source: GridRange
    valueLayout: ValueLayout
    values: List[PivotValue]

class PivotValue(TypedDict):
    "The definition of how a value in a pivot table should be calculated."
    calculatedDisplayType: PivotValueCalculatedDisplayType
    dataSourceColumnReference: DataSourceColumnReference
    formula: str
    name: str
    sourceColumnOffset: int
    summarizeFunction: PivotStandardValueFunction

class ProtectedRange(TypedDict):
    "A protected range."
    description: str
    editors: Editors
    namedRangeId: str
    protectedRangeId: int
    range: GridRange
    requestingUserCanEdit: bool
    unprotectedRanges: List[GridRange]
    warningOnly: bool

class RandomizeRangeRequest(TypedDict):
    "Randomizes the order of the rows in a range."
    range: GridRange

class RefreshDataSourceObjectExecutionStatus(TypedDict):
    "The execution status of refreshing one data source object."
    dataExecutionStatus: DataExecutionStatus
    reference: DataSourceObjectReference

class RefreshDataSourceRequest(TypedDict):
    """
    Refreshes one or multiple data source objects in the spreadsheet by the
    specified references. The request requires an additional bigquery.readonly OAuth
    scope. If there're multiple refresh requests referencing the same data source
    objects in one batch, only the last refresh request is processed, and all those
    requests will have the same response accordingly.
    """
    dataSourceId: str
    force: bool
    isAll: bool
    references: DataSourceObjectReferences

class RefreshDataSourceResponse(TypedDict):
    "The response from refreshing one or multiple data source objects."
    statuses: List[RefreshDataSourceObjectExecutionStatus]

class RepeatCellRequest(TypedDict):
    """
    Updates all cells in the range to the values in the given Cell object. Only the
    fields listed in the fields field are updated; others are unchanged. If writing
    a cell with a formula, the formula's ranges will automatically increment for
    each field in the range. For example, if writing a cell with formula `=A1` into
    range B2:C4, B2 would be `=A1`, B3 would be `=A2`, B4 would be `=A3`, C2 would
    be `=B1`, C3 would be `=B2`, C4 would be `=B3`. To keep the formula's ranges
    static, use the `$` indicator. For example, use the formula `=$A$1` to prevent
    both the row and the column from incrementing.
    """
    cell: CellData
    fields: str
    range: GridRange

class Request(TypedDict, total=False):
    "A single kind of update to apply to a spreadsheet."
    addBanding: AddBandingRequest
    addChart: AddChartRequest
    addConditionalFormatRule: AddConditionalFormatRuleRequest
    addDataSource: AddDataSourceRequest
    addDimensionGroup: AddDimensionGroupRequest
    addFilterView: AddFilterViewRequest
    addNamedRange: AddNamedRangeRequest
    addProtectedRange: AddProtectedRangeRequest
    addSheet: AddSheetRequest
    addSlicer: AddSlicerRequest
    appendCells: AppendCellsRequest
    appendDimension: AppendDimensionRequest
    autoFill: AutoFillRequest
    autoResizeDimensions: AutoResizeDimensionsRequest
    clearBasicFilter: ClearBasicFilterRequest
    copyPaste: CopyPasteRequest
    createDeveloperMetadata: CreateDeveloperMetadataRequest
    cutPaste: CutPasteRequest
    deleteBanding: DeleteBandingRequest
    deleteConditionalFormatRule: DeleteConditionalFormatRuleRequest
    deleteDataSource: DeleteDataSourceRequest
    deleteDeveloperMetadata: DeleteDeveloperMetadataRequest
    deleteDimension: DeleteDimensionRequest
    deleteDimensionGroup: DeleteDimensionGroupRequest
    deleteDuplicates: DeleteDuplicatesRequest
    deleteEmbeddedObject: DeleteEmbeddedObjectRequest
    deleteFilterView: DeleteFilterViewRequest
    deleteNamedRange: DeleteNamedRangeRequest
    deleteProtectedRange: DeleteProtectedRangeRequest
    deleteRange: DeleteRangeRequest
    deleteSheet: DeleteSheetRequest
    duplicateFilterView: DuplicateFilterViewRequest
    duplicateSheet: DuplicateSheetRequest
    findReplace: FindReplaceRequest
    insertDimension: InsertDimensionRequest
    insertRange: InsertRangeRequest
    mergeCells: MergeCellsRequest
    moveDimension: MoveDimensionRequest
    pasteData: PasteDataRequest
    randomizeRange: RandomizeRangeRequest
    refreshDataSource: RefreshDataSourceRequest
    repeatCell: RepeatCellRequest
    setBasicFilter: SetBasicFilterRequest
    setDataValidation: SetDataValidationRequest
    sortRange: SortRangeRequest
    textToColumns: TextToColumnsRequest
    trimWhitespace: TrimWhitespaceRequest
    unmergeCells: UnmergeCellsRequest
    updateBanding: UpdateBandingRequest
    updateBorders: UpdateBordersRequest
    updateCells: UpdateCellsRequest
    updateChartSpec: UpdateChartSpecRequest
    updateConditionalFormatRule: UpdateConditionalFormatRuleRequest
    updateDataSource: UpdateDataSourceRequest
    updateDeveloperMetadata: UpdateDeveloperMetadataRequest
    updateDimensionGroup: UpdateDimensionGroupRequest
    updateDimensionProperties: UpdateDimensionPropertiesRequest
    updateEmbeddedObjectPosition: UpdateEmbeddedObjectPositionRequest
    updateFilterView: UpdateFilterViewRequest
    updateNamedRange: UpdateNamedRangeRequest
    updateProtectedRange: UpdateProtectedRangeRequest
    updateSheetProperties: UpdateSheetPropertiesRequest
    updateSlicerSpec: UpdateSlicerSpecRequest
    updateSpreadsheetProperties: UpdateSpreadsheetPropertiesRequest

class Response(TypedDict, total=False):
    "A single response from an update."
    addBanding: AddBandingResponse
    addChart: AddChartResponse
    addDataSource: AddDataSourceResponse
    addDimensionGroup: AddDimensionGroupResponse
    addFilterView: AddFilterViewResponse
    addNamedRange: AddNamedRangeResponse
    addProtectedRange: AddProtectedRangeResponse
    addSheet: AddSheetResponse
    addSlicer: AddSlicerResponse
    createDeveloperMetadata: CreateDeveloperMetadataResponse
    deleteConditionalFormatRule: DeleteConditionalFormatRuleResponse
    deleteDeveloperMetadata: DeleteDeveloperMetadataResponse
    deleteDimensionGroup: DeleteDimensionGroupResponse
    deleteDuplicates: DeleteDuplicatesResponse
    duplicateFilterView: DuplicateFilterViewResponse
    duplicateSheet: DuplicateSheetResponse
    findReplace: FindReplaceResponse
    refreshDataSource: RefreshDataSourceResponse
    trimWhitespace: TrimWhitespaceResponse
    updateConditionalFormatRule: UpdateConditionalFormatRuleResponse
    updateDataSource: UpdateDataSourceResponse
    updateDeveloperMetadata: UpdateDeveloperMetadataResponse
    updateEmbeddedObjectPosition: UpdateEmbeddedObjectPositionResponse

class RowData(TypedDict):
    "Data about each cell in a row."
    values: List[CellData]

class ScorecardChartSpec(TypedDict):
    """
    A scorecard chart. Scorecard charts are used to highlight key performance
    indicators, known as KPIs, on the spreadsheet. A scorecard chart can represent
    things like total sales, average cost, or a top selling item. You can specify a
    single data value, or aggregate over a range of data. Percentage or absolute
    difference from a baseline value can be highlighted, like changes over time.
    """
    aggregateType: ChartAggregateType
    baselineValueData: ChartData
    baselineValueFormat: BaselineValueFormat
    customFormatOptions: ChartCustomNumberFormatOptions
    keyValueData: ChartData
    keyValueFormat: KeyValueFormat
    numberFormatSource: ChartNumberFormatSource
    scaleFactor: float

class SearchDeveloperMetadataRequest(TypedDict):
    """
    A request to retrieve all developer metadata matching the set of specified
    criteria.
    """
    dataFilters: List[DataFilter]

class SearchDeveloperMetadataResponse(TypedDict):
    "A reply to a developer metadata search request."
    matchedDeveloperMetadata: List[MatchedDeveloperMetadata]

class SetBasicFilterRequest(TypedDict):
    "Sets the basic filter associated with a sheet."
    filter: BasicFilter

class SetDataValidationRequest(TypedDict):
    """
    Sets a data validation rule to every cell in the range. To clear validation in a
    range, call this with no rule specified.
    """
    range: GridRange
    rule: DataValidationRule

class Sheet(TypedDict):
    "A sheet in a spreadsheet."
    bandedRanges: List[BandedRange]
    basicFilter: BasicFilter
    charts: List[EmbeddedChart]
    columnGroups: List[DimensionGroup]
    conditionalFormats: List[ConditionalFormatRule]
    data: List[GridData]
    developerMetadata: List[DeveloperMetadata]
    filterViews: List[FilterView]
    merges: List[GridRange]
    properties: SheetProperties
    protectedRanges: List[ProtectedRange]
    rowGroups: List[DimensionGroup]
    slicers: List[Slicer]

class SheetProperties(TypedDict):
    "Properties of a sheet."
    dataSourceSheetProperties: DataSourceSheetProperties
    gridProperties: GridProperties
    hidden: bool
    index: int
    rightToLeft: bool
    sheetId: int
    sheetType: SheetType
    tabColor: Color
    tabColorStyle: ColorStyle
    title: str

class Slicer(TypedDict):
    "A slicer in a sheet."
    position: EmbeddedObjectPosition
    slicerId: int
    spec: SlicerSpec

class SlicerSpec(TypedDict):
    "The specifications of a slicer."
    applyToPivotTables: bool
    backgroundColor: Color
    backgroundColorStyle: ColorStyle
    columnIndex: int
    dataRange: GridRange
    filterCriteria: FilterCriteria
    horizontalAlignment: HorizontalAlign
    textFormat: TextFormat
    title: str

class SortRangeRequest(TypedDict):
    "Sorts data in rows based on a sort order per column."
    range: GridRange
    sortSpecs: List[SortSpec]

class SortSpec(TypedDict):
    "A sort order associated with a specific column or row."
    backgroundColor: Color
    backgroundColorStyle: ColorStyle
    dataSourceColumnReference: DataSourceColumnReference
    dimensionIndex: int
    foregroundColor: Color
    foregroundColorStyle: ColorStyle
    sortOrder: SortOrder

class SourceAndDestination(TypedDict):
    "A combination of a source range and how to extend that source."
    dimension: Dimension
    fillLength: int
    source: GridRange

class Spreadsheet(TypedDict):
    "Resource that represents a spreadsheet."
    dataSourceSchedules: List[DataSourceRefreshSchedule]
    dataSources: List[DataSource]
    developerMetadata: List[DeveloperMetadata]
    namedRanges: List[NamedRange]
    properties: SpreadsheetProperties
    sheets: List[Sheet]
    spreadsheetId: str
    spreadsheetUrl: str

class SpreadsheetProperties(TypedDict):
    "Properties of a spreadsheet."
    autoRecalc: RecalculationInterval
    defaultFormat: CellFormat
    iterativeCalculationSettings: IterativeCalculationSettings
    locale: str
    spreadsheetTheme: SpreadsheetTheme
    timeZone: str
    title: str

class SpreadsheetTheme(TypedDict):
    "Represents spreadsheet theme"
    primaryFontFamily: str
    themeColors: List[ThemeColorPair]

class TextFormat(TypedDict):
    """
    The format of a run of text in a cell. Absent values indicate that the field
    isn't specified.
    """
    bold: bool
    fontFamily: str
    fontSize: int
    foregroundColor: Color
    foregroundColorStyle: ColorStyle
    italic: bool
    strikethrough: bool
    underline: bool

class TextFormatRun(TypedDict):
    """
    A run of a text format. The format of this run continues until the start index
    of the next run. When updating, all fields must be set.
    """
    format: TextFormat
    startIndex: int

class TextPosition(TypedDict):
    "Position settings for text."
    horizontalAlignment: HorizontalAlign

class TextRotation(TypedDict):
    "The rotation applied to text in a cell."
    angle: int
    vertical: bool

class TextToColumnsRequest(TypedDict):
    """
    Splits a column of text into multiple columns, based on a delimiter in each
    cell.
    """
    delimiter: str
    delimiterType: DelimiterType
    source: GridRange

class ThemeColorPair(TypedDict):
    """
    A pair mapping a spreadsheet theme color type to the concrete color it
    represents.
    """
    color: ColorStyle
    colorType: ThemeColorType

class TimeOfDay(TypedDict):
    """
    Represents a time of day. The date and time zone are either not significant or
    are specified elsewhere. An API may choose to allow leap seconds. Related types
    are google.type.Date and `google.protobuf.Timestamp`.
    """
    hours: int
    minutes: int
    nanos: int
    seconds: int

class TreemapChartColorScale(TypedDict):
    "A color scale for a treemap chart."
    maxValueColor: Color
    maxValueColorStyle: ColorStyle
    midValueColor: Color
    midValueColorStyle: ColorStyle
    minValueColor: Color
    minValueColorStyle: ColorStyle
    noDataColor: Color
    noDataColorStyle: ColorStyle

class TreemapChartSpec(TypedDict):
    "A Treemap chart."
    colorData: ChartData
    colorScale: TreemapChartColorScale
    headerColor: Color
    headerColorStyle: ColorStyle
    hideTooltips: bool
    hintedLevels: int
    labels: ChartData
    levels: int
    maxValue: float
    minValue: float
    parentLabels: ChartData
    sizeData: ChartData
    textFormat: TextFormat

class TrimWhitespaceRequest(TypedDict):
    """
    Trims the whitespace (such as spaces, tabs, or new lines) in every cell in the
    specified range. This request removes all whitespace from the start and end of
    each cell's text, and reduces any subsequence of remaining whitespace characters
    to a single space. If the resulting trimmed text starts with a '+' or '='
    character, the text remains as a string value and isn't interpreted as a
    formula.
    """
    range: GridRange

class TrimWhitespaceResponse(TypedDict):
    "The result of trimming whitespace in cells."
    cellsChangedCount: int

class UnmergeCellsRequest(TypedDict):
    "Unmerges cells in the given range."
    range: GridRange

class UpdateBandingRequest(TypedDict):
    "Updates properties of the supplied banded range."
    bandedRange: BandedRange
    fields: str

class UpdateBordersRequest(TypedDict):
    """
    Updates the borders of a range. If a field is not set in the request, that means
    the border remains as-is. For example, with two subsequent UpdateBordersRequest:
    1. range: A1:A5 `{ top: RED, bottom: WHITE }` 2. range: A1:A5 `{ left: BLUE }`
    That would result in A1:A5 having a borders of `{ top: RED, bottom: WHITE, left:
    BLUE }`. If you want to clear a border, explicitly set the style to NONE.
    """
    bottom: Border
    innerHorizontal: Border
    innerVertical: Border
    left: Border
    range: GridRange
    right: Border
    top: Border

class UpdateCellsRequest(TypedDict):
    "Updates all cells in a range with new data."
    fields: str
    range: GridRange
    rows: List[RowData]
    start: GridCoordinate

class UpdateChartSpecRequest(TypedDict):
    """
    Updates a chart's specifications. (This does not move or resize a chart. To move
    or resize a chart, use UpdateEmbeddedObjectPositionRequest.)
    """
    chartId: int
    spec: ChartSpec

class UpdateConditionalFormatRuleRequest(TypedDict):
    """
    Updates a conditional format rule at the given index, or moves a conditional
    format rule to another index.
    """
    index: int
    newIndex: int
    rule: ConditionalFormatRule
    sheetId: int

class UpdateConditionalFormatRuleResponse(TypedDict):
    "The result of updating a conditional format rule."
    newIndex: int
    newRule: ConditionalFormatRule
    oldIndex: int
    oldRule: ConditionalFormatRule

class UpdateDataSourceRequest(TypedDict):
    """
    Updates a data source. After the data source is updated successfully, an
    execution is triggered to refresh the associated DataSource sheet to read data
    from the updated data source. The request requires an additional
    bigquery.readonly OAuth scope.
    """
    dataSource: DataSource
    fields: str

class UpdateDataSourceResponse(TypedDict):
    "The response from updating data source."
    dataExecutionStatus: DataExecutionStatus
    dataSource: DataSource

class UpdateDeveloperMetadataRequest(TypedDict):
    """
    A request to update properties of developer metadata. Updates the properties of
    the developer metadata selected by the filters to the values provided in the
    DeveloperMetadata resource. Callers must specify the properties they wish to
    update in the fields parameter, as well as specify at least one DataFilter
    matching the metadata they wish to update.
    """
    dataFilters: List[DataFilter]
    developerMetadata: DeveloperMetadata
    fields: str

class UpdateDeveloperMetadataResponse(TypedDict):
    "The response from updating developer metadata."
    developerMetadata: List[DeveloperMetadata]

class UpdateDimensionGroupRequest(TypedDict):
    "Updates the state of the specified group."
    dimensionGroup: DimensionGroup
    fields: str

class UpdateDimensionPropertiesRequest(TypedDict):
    "Updates properties of dimensions within the specified range."
    dataSourceSheetRange: DataSourceSheetDimensionRange
    fields: str
    properties: DimensionProperties
    range: DimensionRange

class UpdateEmbeddedObjectPositionRequest(TypedDict):
    """
    Update an embedded object's position (such as a moving or resizing a chart or
    image).
    """
    fields: str
    newPosition: EmbeddedObjectPosition
    objectId: int

class UpdateEmbeddedObjectPositionResponse(TypedDict):
    "The result of updating an embedded object's position."
    position: EmbeddedObjectPosition

class UpdateFilterViewRequest(TypedDict):
    "Updates properties of the filter view."
    fields: str
    filter: FilterView

class UpdateNamedRangeRequest(TypedDict):
    "Updates properties of the named range with the specified namedRangeId."
    fields: str
    namedRange: NamedRange

class UpdateProtectedRangeRequest(TypedDict):
    "Updates an existing protected range with the specified protectedRangeId."
    fields: str
    protectedRange: ProtectedRange

class UpdateSheetPropertiesRequest(TypedDict):
    "Updates properties of the sheet with the specified sheetId."
    fields: str
    properties: SheetProperties

class UpdateSlicerSpecRequest(TypedDict):
    """
    Updates a slicer's specifications. (This does not move or resize a slicer. To
    move or resize a slicer use UpdateEmbeddedObjectPositionRequest.
    """
    fields: str
    slicerId: int
    spec: SlicerSpec

class UpdateSpreadsheetPropertiesRequest(TypedDict):
    "Updates properties of a spreadsheet."
    fields: str
    properties: SpreadsheetProperties

class UpdateValuesByDataFilterResponse(TypedDict):
    "The response when updating a range of values by a data filter in a spreadsheet."
    dataFilter: DataFilter
    updatedCells: int
    updatedColumns: int
    updatedData: ValueRange
    updatedRange: str
    updatedRows: int

class UpdateValuesResponse(TypedDict):
    "The response when updating a range of values in a spreadsheet."
    spreadsheetId: str
    updatedCells: int
    updatedColumns: int
    updatedData: ValueRange
    updatedRange: str
    updatedRows: int

class ValueRange(TypedDict):
    "Data within a range of the spreadsheet."
    majorDimension: Dimension
    range: str
    values: List[List[Any]]

class WaterfallChartColumnStyle(TypedDict):
    "Styles for a waterfall chart column."
    color: Color
    colorStyle: ColorStyle
    label: str

class WaterfallChartCustomSubtotal(TypedDict):
    "A custom subtotal column for a waterfall chart series."
    dataIsSubtotal: bool
    label: str
    subtotalIndex: int

class WaterfallChartDomain(TypedDict):
    "The domain of a waterfall chart."
    data: ChartData
    reversed: bool

class WaterfallChartSeries(TypedDict):
    "A single series of data for a waterfall chart."
    customSubtotals: List[WaterfallChartCustomSubtotal]
    data: ChartData
    hideTrailingSubtotal: bool
    negativeColumnsStyle: WaterfallChartColumnStyle
    positiveColumnsStyle: WaterfallChartColumnStyle
    subtotalColumnsStyle: WaterfallChartColumnStyle

class WaterfallChartSpec(TypedDict):
    "A waterfall chart."
    connectorLineStyle: LineStyle
    domain: WaterfallChartDomain
    firstValueIsTotal: bool
    hideConnectorLines: bool
    series: List[WaterfallChartSeries]
    stackedType: WaterfallStackedType

Dimension = Union[
    Literal["DIMENSION_UNSPECIFIED"],
    Literal["ROWS"],
    Literal["COLUMNS"],
]

ComparisonType = Union[
    Literal["COMPARISON_TYPE_UNDEFINED"],
    Literal["ABSOLUTE_DIFFERENCE"],
    Literal["PERCENTAGE_DIFFERENCE"],
]

BasicChartAxisPosition = Union[
    Literal["BASIC_CHART_AXIS_POSITION_UNSPECIFIED"],
    Literal["BOTTOM_AXIS"],
    Literal["LEFT_AXIS"],
    Literal["RIGHT_AXIS"],
]

BasicChartType = Union[
    Literal["BASIC_CHART_TYPE_UNSPECIFIED"],
    Literal["BAR"],
    Literal["LINE"],
    Literal["AREA"],
    Literal["COLUMN"],
    Literal["SCATTER"],
    Literal["COMBO"],
    Literal["STEPPED_AREA"],
]

BasicChartCompareMode = Union[
    Literal["BASIC_CHART_COMPARE_MODE_UNSPECIFIED"],
    Literal["DATUM"],
    Literal["CATEGORY"],
]

BasicChartLegendPosition = Union[
    Literal["BASIC_CHART_LEGEND_POSITION_UNSPECIFIED"],
    Literal["BOTTOM_LEGEND"],
    Literal["LEFT_LEGEND"],
    Literal["RIGHT_LEGEND"],
    Literal["TOP_LEGEND"],
    Literal["NO_LEGEND"],
]

BasicChartStackedType = Union[
    Literal["BASIC_CHART_STACKED_TYPE_UNSPECIFIED"],
    Literal["NOT_STACKED"],
    Literal["STACKED"],
    Literal["PERCENT_STACKED"],
]

DateTimeRenderOption = Union[
    Literal["SERIAL_NUMBER"],
    Literal["FORMATTED_STRING"],
]

ValueRenderOption = Union[
    Literal["FORMATTED_VALUE"],
    Literal["UNFORMATTED_VALUE"],
    Literal["FORMULA"],
]

InputValueOption = Union[
    Literal["INPUT_VALUE_OPTION_UNSPECIFIED"],
    Literal["RAW"],
    Literal["USER_ENTERED"],
]

ConditionType = Union[
    Literal["CONDITION_TYPE_UNSPECIFIED"],
    Literal["NUMBER_GREATER"],
    Literal["NUMBER_GREATER_THAN_EQ"],
    Literal["NUMBER_LESS"],
    Literal["NUMBER_LESS_THAN_EQ"],
    Literal["NUMBER_EQ"],
    Literal["NUMBER_NOT_EQ"],
    Literal["NUMBER_BETWEEN"],
    Literal["NUMBER_NOT_BETWEEN"],
    Literal["TEXT_CONTAINS"],
    Literal["TEXT_NOT_CONTAINS"],
    Literal["TEXT_STARTS_WITH"],
    Literal["TEXT_ENDS_WITH"],
    Literal["TEXT_EQ"],
    Literal["TEXT_IS_EMAIL"],
    Literal["TEXT_IS_URL"],
    Literal["DATE_EQ"],
    Literal["DATE_BEFORE"],
    Literal["DATE_AFTER"],
    Literal["DATE_ON_OR_BEFORE"],
    Literal["DATE_ON_OR_AFTER"],
    Literal["DATE_BETWEEN"],
    Literal["DATE_NOT_BETWEEN"],
    Literal["DATE_IS_VALID"],
    Literal["ONE_OF_RANGE"],
    Literal["ONE_OF_LIST"],
    Literal["BLANK"],
    Literal["NOT_BLANK"],
    Literal["CUSTOM_FORMULA"],
    Literal["BOOLEAN"],
    Literal["TEXT_NOT_EQ"],
    Literal["DATE_NOT_EQ"],
]

Style = Union[
    Literal["STYLE_UNSPECIFIED"],
    Literal["DOTTED"],
    Literal["DASHED"],
    Literal["SOLID"],
    Literal["SOLID_MEDIUM"],
    Literal["SOLID_THICK"],
    Literal["NONE"],
    Literal["DOUBLE"],
]

BubbleChartLegendPosition = Union[
    Literal["BUBBLE_CHART_LEGEND_POSITION_UNSPECIFIED"],
    Literal["BOTTOM_LEGEND"],
    Literal["LEFT_LEGEND"],
    Literal["RIGHT_LEGEND"],
    Literal["TOP_LEGEND"],
    Literal["NO_LEGEND"],
    Literal["INSIDE_LEGEND"],
]

HorizontalAlign = Union[
    Literal["HORIZONTAL_ALIGN_UNSPECIFIED"],
    Literal["LEFT"],
    Literal["CENTER"],
    Literal["RIGHT"],
]

HyperlinkDisplayType = Union[
    Literal["HYPERLINK_DISPLAY_TYPE_UNSPECIFIED"],
    Literal["LINKED"],
    Literal["PLAIN_TEXT"],
]

TextDirection = Union[
    Literal["TEXT_DIRECTION_UNSPECIFIED"],
    Literal["LEFT_TO_RIGHT"],
    Literal["RIGHT_TO_LEFT"],
]

VerticalAlign = Union[
    Literal["VERTICAL_ALIGN_UNSPECIFIED"],
    Literal["TOP"],
    Literal["MIDDLE"],
    Literal["BOTTOM"],
]

WrapStrategy = Union[
    Literal["WRAP_STRATEGY_UNSPECIFIED"],
    Literal["OVERFLOW_CELL"],
    Literal["LEGACY_WRAP"],
    Literal["CLIP"],
    Literal["WRAP"],
]

ViewWindowMode = Union[
    Literal["DEFAULT_VIEW_WINDOW_MODE"],
    Literal["VIEW_WINDOW_MODE_UNSUPPORTED"],
    Literal["EXPLICIT"],
    Literal["PRETTY"],
]

ChartAggregateType = Union[
    Literal["CHART_AGGREGATE_TYPE_UNSPECIFIED"],
    Literal["AVERAGE"],
    Literal["COUNT"],
    Literal["MAX"],
    Literal["MEDIAN"],
    Literal["MIN"],
    Literal["SUM"],
]

ChartDateTimeRuleType = Union[
    Literal["CHART_DATE_TIME_RULE_TYPE_UNSPECIFIED"],
    Literal["SECOND"],
    Literal["MINUTE"],
    Literal["HOUR"],
    Literal["HOUR_MINUTE"],
    Literal["HOUR_MINUTE_AMPM"],
    Literal["DAY_OF_WEEK"],
    Literal["DAY_OF_YEAR"],
    Literal["DAY_OF_MONTH"],
    Literal["DAY_MONTH"],
    Literal["MONTH"],
    Literal["QUARTER"],
    Literal["YEAR"],
    Literal["YEAR_MONTH"],
    Literal["YEAR_QUARTER"],
    Literal["YEAR_MONTH_DAY"],
]

ChartHiddenDimensionStrategy = Union[
    Literal["CHART_HIDDEN_DIMENSION_STRATEGY_UNSPECIFIED"],
    Literal["SKIP_HIDDEN_ROWS_AND_COLUMNS"],
    Literal["SKIP_HIDDEN_ROWS"],
    Literal["SKIP_HIDDEN_COLUMNS"],
    Literal["SHOW_ALL"],
]

ThemeColorType = Union[
    Literal["THEME_COLOR_TYPE_UNSPECIFIED"],
    Literal["TEXT"],
    Literal["BACKGROUND"],
    Literal["ACCENT1"],
    Literal["ACCENT2"],
    Literal["ACCENT3"],
    Literal["ACCENT4"],
    Literal["ACCENT5"],
    Literal["ACCENT6"],
    Literal["LINK"],
]

RelativeDate = Union[
    Literal["RELATIVE_DATE_UNSPECIFIED"],
    Literal["PAST_YEAR"],
    Literal["PAST_MONTH"],
    Literal["PAST_WEEK"],
    Literal["YESTERDAY"],
    Literal["TODAY"],
    Literal["TOMORROW"],
]

PasteOrientation = Union[
    Literal["NORMAL"],
    Literal["TRANSPOSE"],
]

PasteType = Union[
    Literal["PASTE_NORMAL"],
    Literal["PASTE_VALUES"],
    Literal["PASTE_FORMAT"],
    Literal["PASTE_NO_BORDERS"],
    Literal["PASTE_FORMULA"],
    Literal["PASTE_DATA_VALIDATION"],
    Literal["PASTE_CONDITIONAL_FORMATTING"],
]

DataExecutionErrorCode = Union[
    Literal["DATA_EXECUTION_ERROR_CODE_UNSPECIFIED"],
    Literal["TIMED_OUT"],
    Literal["TOO_MANY_ROWS"],
    Literal["TOO_MANY_CELLS"],
    Literal["ENGINE"],
    Literal["PARAMETER_INVALID"],
    Literal["UNSUPPORTED_DATA_TYPE"],
    Literal["DUPLICATE_COLUMN_NAMES"],
    Literal["INTERRUPTED"],
    Literal["CONCURRENT_QUERY"],
    Literal["OTHER"],
    Literal["TOO_MANY_CHARS_PER_CELL"],
    Literal["DATA_NOT_FOUND"],
    Literal["PERMISSION_DENIED"],
    Literal["MISSING_COLUMN_ALIAS"],
    Literal["OBJECT_NOT_FOUND"],
    Literal["OBJECT_IN_ERROR_STATE"],
    Literal["OBJECT_SPEC_INVALID"],
]

DataExecutionState = Union[
    Literal["DATA_EXECUTION_STATE_UNSPECIFIED"],
    Literal["NOT_STARTED"],
    Literal["RUNNING"],
    Literal["SUCCEEDED"],
    Literal["FAILED"],
]

DataSourceRefreshScope = Union[
    Literal["DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED"],
    Literal["ALL_DATA_SOURCES"],
]

DayOfWeek = Union[
    Literal["DAY_OF_WEEK_UNSPECIFIED"],
    Literal["MONDAY"],
    Literal["TUESDAY"],
    Literal["WEDNESDAY"],
    Literal["THURSDAY"],
    Literal["FRIDAY"],
    Literal["SATURDAY"],
    Literal["SUNDAY"],
]

DataSourceTableColumnSelectionType = Union[
    Literal["DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED"],
    Literal["SELECTED"],
    Literal["SYNC_ALL"],
]

DateTimeRuleType = Union[
    Literal["DATE_TIME_RULE_TYPE_UNSPECIFIED"],
    Literal["SECOND"],
    Literal["MINUTE"],
    Literal["HOUR"],
    Literal["HOUR_MINUTE"],
    Literal["HOUR_MINUTE_AMPM"],
    Literal["DAY_OF_WEEK"],
    Literal["DAY_OF_YEAR"],
    Literal["DAY_OF_MONTH"],
    Literal["DAY_MONTH"],
    Literal["MONTH"],
    Literal["QUARTER"],
    Literal["YEAR"],
    Literal["YEAR_MONTH"],
    Literal["YEAR_QUARTER"],
    Literal["YEAR_MONTH_DAY"],
]

DeveloperMetadataVisibility = Union[
    Literal["DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED"],
    Literal["DOCUMENT"],
    Literal["PROJECT"],
]

DeveloperMetadataLocationType = Union[
    Literal["DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED"],
    Literal["ROW"],
    Literal["COLUMN"],
    Literal["SHEET"],
    Literal["SPREADSHEET"],
]

DeveloperMetadataLocationMatchingStrategy = Union[
    Literal["DEVELOPER_METADATA_LOCATION_MATCHING_STRATEGY_UNSPECIFIED"],
    Literal["EXACT_LOCATION"],
    Literal["INTERSECTING_LOCATION"],
]

ErrorType = Union[
    Literal["ERROR_TYPE_UNSPECIFIED"],
    Literal["ERROR"],
    Literal["NULL_VALUE"],
    Literal["DIVIDE_BY_ZERO"],
    Literal["VALUE"],
    Literal["REF"],
    Literal["NAME"],
    Literal["NUM"],
    Literal["N_A"],
    Literal["LOADING"],
]

HistogramChartLegendPosition = Union[
    Literal["HISTOGRAM_CHART_LEGEND_POSITION_UNSPECIFIED"],
    Literal["BOTTOM_LEGEND"],
    Literal["LEFT_LEGEND"],
    Literal["RIGHT_LEGEND"],
    Literal["TOP_LEGEND"],
    Literal["NO_LEGEND"],
    Literal["INSIDE_LEGEND"],
]

InterpolationPointType = Union[
    Literal["INTERPOLATION_POINT_TYPE_UNSPECIFIED"],
    Literal["MIN"],
    Literal["MAX"],
    Literal["NUMBER"],
    Literal["PERCENT"],
    Literal["PERCENTILE"],
]

LineDashType = Union[
    Literal["LINE_DASH_TYPE_UNSPECIFIED"],
    Literal["INVISIBLE"],
    Literal["CUSTOM"],
    Literal["SOLID"],
    Literal["DOTTED"],
    Literal["MEDIUM_DASHED"],
    Literal["MEDIUM_DASHED_DOTTED"],
    Literal["LONG_DASHED"],
    Literal["LONG_DASHED_DOTTED"],
]

MergeType = Union[
    Literal["MERGE_ALL"],
    Literal["MERGE_COLUMNS"],
    Literal["MERGE_ROWS"],
]

NumberFormatType = Union[
    Literal["NUMBER_FORMAT_TYPE_UNSPECIFIED"],
    Literal["TEXT"],
    Literal["NUMBER"],
    Literal["PERCENT"],
    Literal["CURRENCY"],
    Literal["DATE"],
    Literal["TIME"],
    Literal["DATE_TIME"],
    Literal["SCIENTIFIC"],
]

OrgChartLabelSize = Union[
    Literal["ORG_CHART_LABEL_SIZE_UNSPECIFIED"],
    Literal["SMALL"],
    Literal["MEDIUM"],
    Literal["LARGE"],
]

PieChartLegendPosition = Union[
    Literal["PIE_CHART_LEGEND_POSITION_UNSPECIFIED"],
    Literal["BOTTOM_LEGEND"],
    Literal["LEFT_LEGEND"],
    Literal["RIGHT_LEGEND"],
    Literal["TOP_LEGEND"],
    Literal["NO_LEGEND"],
    Literal["LABELED_LEGEND"],
]

SortOrder = Union[
    Literal["SORT_ORDER_UNSPECIFIED"],
    Literal["ASCENDING"],
    Literal["DESCENDING"],
]

ValueLayout = Union[
    Literal["HORIZONTAL"],
    Literal["VERTICAL"],
]

PivotValueCalculatedDisplayType = Union[
    Literal["PIVOT_VALUE_CALCULATED_DISPLAY_TYPE_UNSPECIFIED"],
    Literal["PERCENT_OF_ROW_TOTAL"],
    Literal["PERCENT_OF_COLUMN_TOTAL"],
    Literal["PERCENT_OF_GRAND_TOTAL"],
]

PivotStandardValueFunction = Union[
    Literal["PIVOT_STANDARD_VALUE_FUNCTION_UNSPECIFIED"],
    Literal["SUM"],
    Literal["COUNTA"],
    Literal["COUNT"],
    Literal["COUNTUNIQUE"],
    Literal["AVERAGE"],
    Literal["MAX"],
    Literal["MIN"],
    Literal["MEDIAN"],
    Literal["PRODUCT"],
    Literal["STDEV"],
    Literal["STDEVP"],
    Literal["VAR"],
    Literal["VARP"],
    Literal["CUSTOM"],
]

ChartNumberFormatSource = Union[
    Literal["CHART_NUMBER_FORMAT_SOURCE_UNDEFINED"],
    Literal["FROM_DATA"],
    Literal["CUSTOM"],
]

SheetType = Union[
    Literal["SHEET_TYPE_UNSPECIFIED"],
    Literal["GRID"],
    Literal["OBJECT"],
    Literal["DATA_SOURCE"],
]

RecalculationInterval = Union[
    Literal["RECALCULATION_INTERVAL_UNSPECIFIED"],
    Literal["ON_CHANGE"],
    Literal["MINUTE"],
    Literal["HOUR"],
]

DelimiterType = Union[
    Literal["DELIMITER_TYPE_UNSPECIFIED"],
    Literal["COMMA"],
    Literal["SEMICOLON"],
    Literal["PERIOD"],
    Literal["SPACE"],
    Literal["CUSTOM"],
    Literal["AUTODETECT"],
]

WaterfallStackedType = Union[
    Literal["WATERFALL_STACKED_TYPE_UNSPECIFIED"],
    Literal["STACKED"],
    Literal["SEQUENTIAL"],
]

InsertDataOption = Union[
    Literal["OVERWRITE"],
    Literal["INSERT_ROWS"],
]

