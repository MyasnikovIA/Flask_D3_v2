<div cmptype="Form"  name="MAINFORM" width="60%" height="60%"  caption="Примеры использования Tree (дописать)" >
    <!--

    http://javascript.ru/files/upload/tree/tree_example.html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head><TITLE>Tree Example</TITLE>
<script type="text/javascript">

function tree_toggle(event) {
        event = event || window.event
        var clickedElem = event.target || event.srcElement

        if (!hasClass(clickedElem, 'Expand')) {
                return // клик не там
        }

        // Node, на который кликнули
        var node = clickedElem.parentNode
        if (hasClass(node, 'ExpandLeaf')) {
                return // клик на листе
        }

        // определить новый класс для узла
        var newClass = hasClass(node, 'ExpandOpen') ? 'ExpandClosed' : 'ExpandOpen'
        // заменить текущий класс на newClass
        // регексп находит отдельно стоящий open|close и меняет на newClass
        var re =  /(^|\s)(ExpandOpen|ExpandClosed)(\s|$)/
        node.className = node.className.replace(re, '$1'+newClass+'$3')
}


function hasClass(elem, className) {
        return new RegExp("(^|\\s)"+className+"(\\s|$)").test(elem.className)
}
</script>

<style type="text/css">

.Container {
    padding: 0;
    margin: 0;
}

.Container li {
    list-style-type: none;
}


/* indent for all tree children excepts root */
.Node {
    background-image : url(img/i.gif);
    background-position : top left;
    background-repeat : repeat-y;
    margin-left: 18px;
    zoom: 1;
}

.IsRoot {
    margin-left: 0;
}


/* left vertical line (grid) for all nodes */
.IsLast {
    background-image: url(img/i_half.gif);
    background-repeat : no-repeat;
}

.ExpandOpen .Expand {
    background-image: url(img/expand_minus.gif);
}

/* closed is higher priority than open */
.ExpandClosed .Expand {
    background-image: url(img/expand_plus.gif);
}

/* highest priority */
.ExpandLeaf .Expand {
    background-image: url(img/expand_leaf.gif);
}

.Content {
    min-height: 18px;
    margin-left:18px;
}

* html .Content {
    height: 18px;
}

.Expand {
    width: 18px;
    height: 18px;
    float: left;
}


.ExpandOpen .Container {
        display: block;
}

.ExpandClosed .Container {
        display: none;
}

.ExpandOpen .Expand, .ExpandClosed .Expand {
        cursor: pointer;
}
.ExpandLeaf .Expand {
        cursor: auto;
}

</style>
</head>
<body>

<div onclick="tree_toggle(arguments[0])">
<div>Tree</div>
<ul class="Container">
  <li class="Node IsRoot IsLast ExpandClosed">
    <div class="Expand"></div>
    <div class="Content">Root</div>
    <ul class="Container">
      <li class="Node ExpandClosed">
        <div class="Expand"></div>
        <div class="Content">Item 1</div>
        <ul class="Container">
          <li class="Node ExpandLeaf IsLast">
            <div class="Expand"></div>
            <div class="Content">Item 1.2</div>
          </li>
        </ul>
      </li>
      <li class="Node ExpandLeaf IsLast">
        <div class="Expand"></div>
        <div class="Content">Item 2</div>
      </li>
    </ul>
  </li>
</ul>

</div>


</body>
</html>

    -->

</div>
