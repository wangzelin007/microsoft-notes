(function($) {
  const
    cellValue = (row, index) => index !== -1 ? $(row).children('td').eq(index).text() : 0,
    compareCells = (index, options) =>
      (rowA, rowB) => {
        const colOpts = options[index] || {};
        let
          a = cellValue(rowA, index),
          b = cellValue(rowB, index);
        if (colOpts.dateFormat) {
          a = moment(a, colOpts.dateFormat).valueOf(),
          b = moment(b, colOpts.dateFormat).valueOf()
        }
        return $.isNumeric(a) && $.isNumeric(b) ? a - b : a.toString().localeCompare(b);
      };
  Object.assign($.fn, {
    scanSelectOptionData: function() {
      return [...this.get(0).options].reduce((acc, option, index) => {
        const colOpts = {};
        if (option.dataset.dateFormat) {
          colOpts.dateFormat = option.dataset.dateFormat;
        }
        return { ...acc, [option.value]: colOpts };
      });
    },
    sortTable: function(columnIndex, opts, reverse) {
      let rows = this.find('tbody tr').toArray().sort(compareCells(columnIndex, opts));
      return this.append(reverse ? rows.reverse() : rows);
    }
  });
})(jQuery);

$(document).ready(function() {
  const
    $table = $('#myTable'),
    $select = $('#nameselect > select'),
    $radio = $('input[name="sort-direction"]');

  const sortTable = () => {
    const
      columnIndex = parseInt($select.val(), 10),
      opts = $select.scanSelectOptionData(),
      reverse = $('input[name="sort-direction"]:checked').val() === 'DESC';
    $table.sortTable(columnIndex, opts, reverse);
  };

//  const sortTable = () => {
//    const
//      columnIndex = 0,
//      opts = $select.scanSelectOptionData(),
//      reverse = $('input[name="sort-direction-1"]:checked').val() === 'DESC';
//    $table.sortTable(columnIndex, opts, reverse);
//  };
//
//  const sortTable = () => {
//    const
//      columnIndex = 1,
//      opts = $select.scanSelectOptionData(),
//      reverse = $('input[name="sort-direction-2"]:checked').val() === 'DESC';
//    $table.sortTable(columnIndex, opts, reverse);
//  };
//
//  const sortTable = () => {
//    const
//      columnIndex = 2,
//      opts = $select.scanSelectOptionData(),
//      reverse = $('input[name="sort-direction-3"]:checked').val() === 'DESC';
//    $table.sortTable(columnIndex, opts, reverse);
//  };
//
//  const sortTable = () => {
//    const
//      columnIndex = 3,
//      opts = $select.scanSelectOptionData(),
//      reverse = $('input[name="sort-direction-4"]:checked').val() === 'DESC';
//    $table.sortTable(columnIndex, opts, reverse);
//  };

  $select.on('change', sortTable);
  $radio.on('change', sortTable);
});