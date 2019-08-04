'use-strict'

document.querySelectorAll('input[type="checkbox"]')[0].checked = true;
document.querySelectorAll('input[type="checkbox"]')[1].checked = true;
document.querySelectorAll('input[type="radio"]')[0].checked = true;
document.querySelectorAll('input[type="radio"]')[1].checked = true;
document.querySelectorAll('select > option')[2].selected = true;

const div = document.querySelector('div')
div.addEventListener('mousemove', e => {
  // イベントのx座標y座標を取得し、テンプレートリテラルで埋め込む
  div.textContent = `${e.clientX}:${e.clientY}`;
});

const a = document.querySelector('a');
const span = document.querySelector('span');

a.addEventListener('click', e => {
  e.preventDefault();//要素の規定の動作をキャンセルする。ここではaタグのhref=""へのページ遷移をキャンセル
  a.classList.add('hidden');
  span.classList.remove('hidden');
});