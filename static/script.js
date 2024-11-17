
        function toggleEdit() {
            const inputs = document.querySelectorAll('.editable');
            const addRowButton = document.getElementById('add-row-button');

            inputs.forEach(input => {
                input.disabled = !input.disabled; // Toggle the disabled attribute
                if (!input.disabled) {
                    input.style.border = "1px solid #4a90e2"; // Highlight editable fields
                    input.style.backgroundColor = "#f9f9f9";
                } else {
                    input.style.border = "none"; // Reset styling when not editable
                    input.style.backgroundColor = "transparent";
                }
            });

            // Toggle visibility of the Add Row button
            if (addRowButton.style.display === "none" || !addRowButton.style.display) {
                addRowButton.style.display = "block";
            } else {
                addRowButton.style.display = "none";
            }
        }

        function addRow() {
            const table = document.getElementById('schedule-table').querySelector('tbody');
            const newRow = document.createElement('tr');

            newRow.innerHTML = `
                <td><input type="text" value="New Room" class="editable"></td>
                <td><input type="text" value="New Time" class="editable"></td>
                <td><input type="checkbox" class="attendance-checkbox">
                    <label class="attendance-button"></label></td>
            `;

            table.appendChild(newRow);
        }
    