import React, { useState, useEffect } from 'react';
import jsonFetchData from './api';


//  Components
const TopicSideBar = ({filter, setFilter}) => {
    return (
        <div className="inner-wrapper">
            <div className="inner-sidebar">
                <div className="inner-sidebar-header justify-content-center">
                    <a className="btn btn-primary has-icon btn-block" href="/topics/new/">New topic</a>
                </div>
                <div className="inner-sidebar-body p-0">
                    <div className="p-3 h-100" data-simplebar="init">
                        <nav className="nav nav-pills nav-gap-y-1 flex-column">
                            <a href="#" onClick={() => setFilter("all")} className={`nav-link nav-link-faded has-icon ${filter == 'all' ? "active" : ""}`}>
                                All Threads
                            </a>
                            <a href="#" onClick={() => setFilter("solved")} className={`nav-link nav-link-faded has-icon ${filter == 'solved' ? "active" : ""}`}>Solved</a>
                            <a href="#" onClick={() => setFilter("unsolved")} className={`nav-link nav-link-faded has-icon ${filter == 'unsolved' ? "active" : ""}`}>Unsolved</a>
                            <a href="#" onClick={() => setFilter("noreplies")} className={`nav-link nav-link-faded has-icon ${filter == 'noreplies' ? "active" : ""}`}>No replies yet</a>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    )
}

const TopicHeader = ({search, setSearch}) => {
    const [searchInput, setSearchInput] = useState(search);

    return (
        <div className="inner-main-header">
            <span className="input-icon input-icon-sm ml-auto w-auto">
                <form onSubmit={(event) => {event.preventDefault(); setSearch(searchInput);}}>
                    <div className="form-row align-items-center">
                        <div className="col-auto">
                            <input type="text" name="search" className="form-control bg-gray-200 border-gray-200 shadow-none"
                                placeholder="Search forum" onChange={(event) => setSearchInput(event.target.value)} value={searchInput} />
                        </div>
                        <div className="col-auto">
                            <input type="submit" className="btn btn-primary has-icon btn-block" value="Search" />
                        </div>
                    </div>
                </form>
            </span>
        </div>
    )
}

const TopicListItem = ({topic, search, filter}) => {
    return (
        <div className="card mb-2">
            <div className="card-body p-2 p-sm-3">
                <div className="media forum-item">
                    <img src={topic.creator_serializer.avatar} className="mr-3 rounded-circle"
                        width="50" alt="User" />
                    <div className="media-body">
                        <h6 className="text-body"><a className="text-dark" href={`/topics/${topic.id}/react/?search=${search}&filter=${filter}`}>{topic.title}</a></h6>
                        <p className="text-secondary">
                            {topic.description}
                        </p>
                        <div className="text-muted">
                            {topic.topicmessage_last ? (
                                <div>
                                    <span className="text-secondary font-weight-bold">{topic.topicmessage_last.creator_name} </span>
                                    replied
                                    <span className="text-secondary font-weight-bold"> {topic.topicmessage_last.created_at}</span>
                                </div>
                            ) : (
                                <div>no reply</div>
                            )}
                        </div>
                    </div>
                    <div className="text-muted small text-center align-self-center">
                        <span><i className="far fa-comment ml-2"></i> {topic.topicmessage_count}</span>
                    </div>
                </div>
            </div>
        </div>
    )
}

const TopicList = ({props}) => {
    const [filter, setFilter] = useState(props.filter || "all");
    const [search, setSearch] = useState(props.search || "");
    const [nextUrl, setNextUrl] = useState();
    const [result, setResult] = useState([]);

    useEffect(async () => {
        await fetchTopicList()
    }, [filter, search]);
    
    const fetchTopicList = async (url=null) => {
        const fetchUrl = url ? url : `/api/topic/?search=${search}&filter=${filter}`;
        const response = await jsonFetchData(fetchUrl);
        setNextUrl(response.next)
        setResult(url ? [...result, ...response.results] : response.results)
    }

    return (
        <div className="inner-wrapper">
            <TopicSideBar filter={filter} search={search} setFilter={setFilter}/>

            <div className="inner-main">
                <TopicHeader filter={filter} search={search} setSearch={setSearch} />
                <div className="inner-main-body p-2 p-sm-3 collapse forum-content show">
                    {result && (
                        <div>
                            {result.map(topic => <TopicListItem key={`topic-${topic.id}`} topic={topic} search={search} filter={filter}/>)}
                            {nextUrl && <button onClick={() => fetchTopicList(nextUrl)} className="btn btn-primary btn-block">More</button>}
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
}

export default TopicList