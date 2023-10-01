(()=>{"use strict";var t={496:t=>{t.exports=require("vscode")},81:t=>{t.exports=require("child_process")},147:t=>{t.exports=require("fs")},17:t=>{t.exports=require("path")}},e={};function s(i){var o=e[i];if(void 0!==o)return o.exports;var r=e[i]={exports:{}};return t[i](r,r.exports,s),r.exports}var i={};(()=>{var t=i;Object.defineProperty(t,"__esModule",{value:!0}),t.deactivate=t.activate=void 0;const e=s(17),o=s(147),r=s(81),n=s(496);function a(t){return new Promise(((e,s)=>{o.exists(t,(t=>{e(t)}))}))}const c=["build","compile","watch"];function u(t){for(const e of c)if(-1!==t.indexOf(e))return!0;return!1}const d=["test"];function h(t){for(const e of d)if(-1!==t.indexOf(e))return!0;return!1}let f,l;function p(){return f||(f=n.window.createOutputChannel("Jake Auto Detection")),f}function k(){n.window.showWarningMessage(n.l10n.t("Problem finding jake tasks. See the output for more information."),n.l10n.t("Go to output")).then((()=>{p().show(!0)}))}async function w(t){let s;const i=process.platform;return s="win32"===i&&await a(e.join(t,"node_modules",".bin","jake.cmd"))?e.join(".","node_modules",".bin","jake.cmd"):"linux"!==i&&"darwin"!==i||!await a(e.join(t,"node_modules",".bin","jake"))?"jake":e.join(".","node_modules",".bin","jake"),s}class b{constructor(t,e){this.c=t,this.d=e}get workspaceFolder(){return this.c}isEnabled(){return"on"===n.workspace.getConfiguration("jake",this.c.uri).get("autoDetect")}start(){const t=e.join(this.c.uri.fsPath,"{node_modules,Jakefile,Jakefile.js}");this.a=n.workspace.createFileSystemWatcher(t),this.a.onDidChange((()=>this.b=void 0)),this.a.onDidCreate((()=>this.b=void 0)),this.a.onDidDelete((()=>this.b=void 0))}async getTasks(){return this.isEnabled()?(this.b||(this.b=this.e()),this.b):[]}async getTask(t){const e=t.definition.task;if(e){const s=t.definition,i={cwd:this.workspaceFolder.uri.fsPath};return new n.Task(s,this.workspaceFolder,e,"jake",new n.ShellExecution(await this.d,[e],i))}}async e(){const t="file"===this.c.uri.scheme?this.c.uri.fsPath:void 0,s=[];if(!t)return s;let i=e.join(t,"Jakefile");if(!await a(i)&&(i=e.join(t,"Jakefile.js"),!await a(i)))return s;const o=`${await this.d} --tasks`;try{const{stdout:e,stderr:s}=await(c=o,d={cwd:t},new Promise(((t,e)=>{r.exec(c,d,((s,i,o)=>{s&&e({error:s,stdout:i,stderr:o}),t({stdout:i,stderr:o})}))})));s&&(p().appendLine(s),k());const i=[];if(e){const t=e.split(/\r{0,1}\n/);for(const e of t){if(0===e.length)continue;const t=/^jake\s+([^\s]+)\s/g.exec(e);if(t&&2===t.length){const s=t[1],o={type:"jake",task:s},r={cwd:this.workspaceFolder.uri.fsPath},a=new n.Task(o,s,"jake",new n.ShellExecution(`${await this.d} ${s}`,r));i.push(a);const c=e.toLowerCase();u(c)?a.group=n.TaskGroup.Build:h(c)&&(a.group=n.TaskGroup.Test)}}}return i}catch(t){const e=p();return t.stderr&&e.appendLine(t.stderr),t.stdout&&e.appendLine(t.stdout),e.appendLine(n.l10n.t("Auto detecting Jake for folder {0} failed with error: {1}', this.workspaceFolder.name, err.error ? err.error.toString() : 'unknown")),k(),s}var c,d}dispose(){this.b=void 0,this.a&&this.a.dispose()}}class g{constructor(){this.b=new Map}start(){const t=n.workspace.workspaceFolders;t&&this.c(t,[]),n.workspace.onDidChangeWorkspaceFolders((t=>this.c(t.added,t.removed))),n.workspace.onDidChangeConfiguration(this.d,this)}dispose(){this.a&&(this.a.dispose(),this.a=void 0),this.b.clear()}c(t,e){for(const t of e){const e=this.b.get(t.uri.toString());e&&(e.dispose(),this.b.delete(t.uri.toString()))}for(const e of t){const t=new b(e,w(e.uri.fsPath));this.b.set(e.uri.toString(),t),t.isEnabled()&&t.start()}this.e()}d(){for(const t of this.b.values())t.dispose(),this.b.delete(t.workspaceFolder.uri.toString());const t=n.workspace.workspaceFolders;if(t)for(const e of t)if(!this.b.has(e.uri.toString())){const t=new b(e,w(e.uri.fsPath));this.b.set(e.uri.toString(),t),t.isEnabled()&&t.start()}this.e()}e(){if(!this.a&&this.b.size>0){const t=this;this.a=n.tasks.registerTaskProvider("jake",{provideTasks:()=>t.getTasks(),resolveTask:e=>t.getTask(e)})}else this.a&&0===this.b.size&&(this.a.dispose(),this.a=void 0)}getTasks(){return this.f()}f(){if(0===this.b.size)return Promise.resolve([]);if(1===this.b.size)return this.b.values().next().value.getTasks();{const t=[];for(const e of this.b.values())t.push(e.getTasks().then((t=>t),(()=>[])));return Promise.all(t).then((t=>{const e=[];for(const s of t)s&&s.length>0&&e.push(...s);return e}))}}async getTask(t){if(0!==this.b.size){if(1===this.b.size)return this.b.values().next().value.getTask(t);if(t.scope!==n.TaskScope.Workspace&&t.scope!==n.TaskScope.Global&&t.scope){const e=this.b.get(t.scope.uri.toString());if(e)return e.getTask(t)}}}}t.activate=function(t){l=new g,l.start()},t.deactivate=function(){l.dispose()}})();var o=exports;for(var r in i)o[r]=i[r];i.__esModule&&Object.defineProperty(o,"__esModule",{value:!0})})();
//# sourceMappingURL=https://ticino.blob.core.windows.net/sourcemaps/abd2f3db4bdb28f9e95536dfa84d8479f1eb312d/extensions/jake/dist/main.js.map