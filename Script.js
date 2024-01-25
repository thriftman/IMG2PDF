document.addEventListener('DOMContentLoaded', function () {
    const imageInput = document.getElementById('imageInput');
    const previewContainer = document.getElementById('preview');
    const previewImage = document.createElement('img');

    imageInput.addEventListener('change', function () {
        const file = this.files[0];

        if (file) {
            const reader = new FileReader();

            reader.onload = function (e) {
                previewImage.src = e.target.result;
                previewImage.classList.add('img-fluid');
                previewContainer.innerHTML = ''; // Clear previous preview
                previewContainer.appendChild(previewImage);
            };

            reader.readAsDataURL(file);
        }
    });
});
