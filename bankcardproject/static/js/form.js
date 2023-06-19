// static/js/form.js
document.addEventListener('DOMContentLoaded', () => {
  const districtSelect = document.getElementById('district');
  const branchSelect = document.getElementById('branch');

  districtSelect.addEventListener('change', () => {
    const district = districtSelect.value;
    const branches = getBranches
