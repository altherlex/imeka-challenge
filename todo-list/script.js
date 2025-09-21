$(document).ready(function() {
  $("#addBtn").click(function() {
    const taskText = $("#taskInput").val().trim();
    if (taskText === "") return;

    const $li = $("<li></li>").text(taskText);
    const $delBtn = $("<button></button>").text("Delete");

    $delBtn.on("click", function() {
      $li.remove();
    });

    $li.append($delBtn);
    $("#taskList").append($li);

    $("#taskInput").val("").focus();
  });
});
