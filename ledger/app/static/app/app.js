document.addEventListener("DOMContentLoaded", function () {

    document.querySelector("#new-trans").addEventListener("click", () => {
        document.querySelector("#container-main").style.display = "none";
        document.querySelector("#new-transactions").style.display = "block";
        
    });
    load_trans();

    document.querySelector("#cancel-btn").addEventListener("click", () => {
            document.querySelector("#new-transactions").style.display = "none";
            document.querySelector("#container-main").style.display = "block";
        });
    
    document.querySelector("#sort-btn").addEventListener("click", () => {
        document.getElementById("close-btn").click();
        var cat = document.getElementsByName("categorie")[0].value;
        var min = document.getElementsByName("min")[0].value;
        var max = document.getElementsByName("max")[0].value;
        var after = document.getElementsByName("after")[0].value;
        var before = document.getElementsByName("before")[0].value;

        const data = new FormData();
        data.append("categorie", cat);
        data.append("min", min);
        data.append("max", max);
        data.append("after", after);
        data.append("before", before);

        fetch('/get_data', {
            method: "POST",
            body: data
        })
        .then(response => response.json())
        .then(transactions => {
            load_tables(transactions);
        })
    });
});


function load_trans() {
    fetch('/get_data')
    .then(response => response.json())
    .then(transactions => {
        load_tables(transactions);
    })
    false;
}

function load_tables(trans) {
    var container = document.querySelector("#table-data");
    container.innerHTML = '';
    trans.forEach(element => {
        var row = document.createElement('tr');
        var col1 = document.createElement('td');
        var col2 = document.createElement('td');
        var col3 = document.createElement('td');
        var col4 = document.createElement('td');
        var col5 = document.createElement('td');

        col1.innerHTML = element.cat;
        col2.innerHTML = element.description;
        col3.innerHTML = element.amount;
        col4.innerHTML = element.to;
        col5.innerHTML = element.date;

        row.appendChild(col1);
        row.appendChild(col2);
        row.appendChild(col3);
        row.appendChild(col4);
        row.appendChild(col5);

        container.appendChild(row);

    });
}